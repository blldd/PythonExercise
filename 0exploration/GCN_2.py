# coding=gbk
import numpy as np
import argparse
import torch
from torch.autograd import Variable
import torch.nn.functional as F     #激励函数
import pandas as pd
import re
import math
import scipy.sparse as sp
from sklearn import preprocessing
from torch.nn.parameter import Parameter
from sklearn.model_selection import train_test_split
from scipy.io import loadmat

class GraphConvolution(torch.nn.Module):
    """
    Simple GCN layer, similar to https://arxiv.org/abs/1609.02907
    """
    def __init__(self, in_features, out_features, bias=True):
        super(GraphConvolution, self).__init__()
        self.in_features = in_features
        self.out_features = out_features
        self.weight = Parameter(torch.FloatTensor(in_features, out_features))
        if bias:
            self.bias = Parameter(torch.FloatTensor(out_features))
        else:
            self.register_parameter('bias', None)
        self.reset_parameters()

    def reset_parameters(self):
        stdv = 1. / math.sqrt(self.weight.size(1))
        self.weight.data.uniform_(-stdv, stdv)
        if self.bias is not None:
            self.bias.data.uniform_(-stdv, stdv)

    def forward(self, input, adj):
        support = torch.mm(input, self.weight)
        output = torch.spmm(adj, support)
        if self.bias is not None:
            return output + self.bias
        else:
            return output

    def __repr__(self):
        return self.__class__.__name__ + ' (' \
               + str(self.in_features) + ' -> ' \
               + str(self.out_features) + ')'


class Model(torch.nn.Module):
    def __init__(self, n_feature, n_hidden, n_output,u_input,movie,user,dropout):
        super(Model, self).__init__()
        self.gc1 = GraphConvolution(n_feature, n_hidden)  # 隐藏层线性输出
        self.gc2 = GraphConvolution(n_hidden, n_output)  # 输出层线性输出
        self.pre=torch.nn.Linear(n_output+u_input,1)
        self.movie=movie
        self.user=user
        self.dropout=dropout

    def forward(self,adj,user_movie):
        h_1 = F.relu(self.gc1(self.movie, adj))
        h_2 = self.gc2(h_1, adj)
        pred = self.pre(h_2, )
        #a = torch.reshape(torch.tensor(range(12)), [3, 4])
        #li=[1,2,1]
        #a[li]
        x_1 = h_2[user_movie[:,1]-1,:]
        x_2 = self.user[user_movie[:,0]-1,:]
        x=torch.cat((x_1,x_2),1)
        r = torch.sigmoid(self.pre(x))            # 激励函数(隐藏层的线性值)
        return r

    def backward(self):
        pass


def load_data():
    # 读取User数据
    users_title = ['UserID', 'Gender', 'Age', 'JobID', 'Zip-code']
    users = pd.read_csv('d:\\document\\pycharm\\read\\do\\users.dat', sep='::', header=None, names=users_title,
                          engine='python')
    users = users.filter(regex='UserID|Gender|Age|JobID')
    users_orig = users.values
    # 改变User数据中性别和年龄
    gender_map = {'F': 0, 'M': 1}
    users['Gender'] = users['Gender'].map(gender_map)

    age_map = {val: ii for ii, val in enumerate(set(users['Age']))}
    users['Age'] = users['Age'].map(age_map)

    # 读取Movie数据集
    movies_title = ['MovieID', 'Title', 'Genres']
    movies = pd.read_csv('d:\\document\\pycharm\\read\\do\\movies.dat', sep='::', header=None, names=movies_title,
                           engine='python')
    movies_orig = movies.values
    # 将Title中的年份去掉
    pattern = re.compile(r'^(.*)\((\d+)\)$')

    title_map = {val: pattern.match(val).group(1) for ii, val in enumerate(set(movies['Title']))}
    movies['Title'] = movies['Title'].map(title_map)

    genres_set = set()
    for val in movies['Genres'].str.split('|'):
        genres_set.update(val)
    genres_set.add('<PAD>')
    genres2int = {val: ii for ii, val in enumerate(genres_set)}

    # 将电影类型转成等长数字列表，长度是18
    genres_map = {val: [genres2int[row] for row in val.split('|')] for ii, val in enumerate(set(movies['Genres']))}
    for key in genres_map:
        for cnt in range(max(genres2int.values()) - len(genres_map[key])):
            genres_map[key].insert(len(genres_map[key]) + cnt, genres2int['<PAD>'])

    movies['Genres'] = movies['Genres'].map(genres_map)

    # 电影Title转数字字典
    title_set = set()
    for val in movies['Title'].str.split():
        title_set.update(val)

    title_set.add('<PAD>')
    title2int = {val: ii for ii, val in enumerate(title_set)}

    # 将电影Title转成等长数字列表，长度是15
    title_count = 15
    title_map = {val: [title2int[row] for row in val.split()] for ii, val in enumerate(set(movies['Title']))}

    for key in title_map:
        for cnt in range(title_count - len(title_map[key])):
            title_map[key].insert(len(title_map[key]) + cnt, title2int['<PAD>'])

    movies['Title'] = movies['Title'].map(title_map)

    # 读取评分数据集
    ratings_title = ['UserID', 'MovieID', 'ratings', 'timestamps']
    ratings = pd.read_csv('d:\\document\\pycharm\\read\\do\\ratings.dat', sep='::', header=None, names=ratings_title,
                            engine='python')
    # ratings = ratings.filter(regex='UserID|MovieID|ratings')

    # 合并三个表
    data = pd.merge(pd.merge(ratings, users), movies)

    # 将数据分成X和y两张表
    target_fields = ['ratings']
    features_pd, targets_pd = data.drop(target_fields, axis=1), data[target_fields]

    features = features_pd.values
    targets_values = targets_pd.values

    # title_count  标题转数字，维度15
    # title_set 标题单词集合
    # genres2int 电影类型表，维度19
    # user 用户信息

    return title_count, title_set, genres2int, features, targets_values, ratings, users, movies, data, movies_orig, users_orig

def one_hot(features, ratings,movies,users):
    features_id = features[0:1, :];
    features_vec = features[3:7, :];
    movies_count = movies.shape[0];#电影个数
    users_count=users.shape[0];#用户个数
    user_sex = np.zeros([users_count, 2], dtype=float)
    user_age = np.zeros([users_count, 7], dtype=float)
    user_job = np.zeros([users_count, 21], dtype=float)
    movie_title = np.zeros([movies_count, 15], dtype=float)
    movie_genres = np.zeros([movies_count, 18], dtype=float)
#    rat = np.zeros([features_count], dtype=int)
    for i in range(users_count):
        if(i%1000==0):print(i)
        user_sex[i, users[i, 1]] = 1;
        user_age[i, users[i, 2]] = 1;
        user_job[i, users[i, 3]] = 1;
    for i in range(movies_count):
        movie_title[i, :] = np.array(movies[i, 1])
        movie_genres[i, :] = np.array(movies[i, 2])

    fea_user = np.hstack((user_sex, user_age, user_job,))
    fea_movie = np.hstack((movie_title,movie_genres))
    fea_user = preprocessing.scale(fea_user);#预处理，标准化
    fea_movie = preprocessing.scale(fea_movie);
    return fea_movie, fea_user

def normalize(mx):
    """Row-normalize sparse matrix"""
    rowsum = np.array(mx.sum(1))
    r_inv = np.power(rowsum, -1).flatten()
    r_inv[np.isinf(r_inv)] = 0.
    r_mat_inv = sp.diags(r_inv)
    mx = r_mat_inv.dot(mx)
    return mx

def sparse_mx_to_torch_sparse_tensor(sparse_mx):
    """Convert a scipy sparse matrix to a torch sparse tensor."""
    sparse_mx = sparse_mx.tocoo().astype(np.float32)
    indices = torch.from_numpy(
        np.vstack((sparse_mx.row, sparse_mx.col)).astype(np.int64))
    values = torch.from_numpy(sparse_mx.data)
    shape = torch.Size(sparse_mx.shape)
    return torch.sparse.FloatTensor(indices, values, shape)

def train(adj,movies,users,x_train,y_train):
    train_count = x_train.shape[0];  #评分样本个数
    m_input_data = movies.shape[1];  # 电影输入层维度
    m_hidden_layer = 60  #电影 隐藏层维度
    m_output_data = 30  # 电影输出层维度
    u_input_data=users.shape[1];#用户输入维度

    movies = Variable(torch.from_numpy(movies), requires_grad=True);
    users = Variable(torch.from_numpy(users), requires_grad=True);
    movies=movies.float();users=users.float();
    y = Variable(torch.from_numpy(y_train), requires_grad=True);
    epoch_n = 20;  # 训练次数
    n_bath = 4000;  # 批量梯度下降批次数
    learning_rate = 5*1e-3;
    bath = train_count // n_bath;


    model = Model(m_input_data, m_hidden_layer, m_output_data,u_input_data, movies, users,dropout=args.dropout);
    optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)
    loss_fn = torch.nn.MSELoss(reduce=True, size_average=True)  # MSE损失

    for epoch in range(epoch_n):
        for j in range(n_bath):
            index=np.array(range(j*bath,(j+1)*bath))
            xx=x_train[index];
            yy=y[index,2];
            yy=yy.float()/4;
            yy_pred = model.forward(adj,xx)

            loss = loss_fn(yy_pred.float(), yy.float())

            print("Epoch:{} , N_bath:{},Loss:{:.4f}".format(epoch, j,loss.data))
            if(loss.data<0.01):return model;
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
    return model
if __name__ == "__main__":
    '''''
    print('start')
    title_count, title_set, genres2int, features, targetsv_alues, _, users, movies, data, movies_orig, users_orig = load_data()
    print("read over")
    ratings = data['ratings'];
    movies=np.array(movies);users=np.array(users);
    fea_movie, fea_user=one_hot(features, ratings,movies,users);
    np.save('fea_movie.npy',fea_movie);
    np.save('fea_user.npy',fea_user);
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('--no-cuda', action='store_true', default=False,
                        help='Disables CUDA training.')
    parser.add_argument('--fastmode', action='store_true', default=False,
                        help='Validate during training pass.')
    parser.add_argument('--seed', type=int, default=42, help='Random seed.')
    parser.add_argument('--epochs', type=int, default=200,
                        help='Number of epochs to train.')
    parser.add_argument('--lr', type=float, default=0.01,
                        help='Initial learning rate.')
    parser.add_argument('--weight_decay', type=float, default=5e-4,
                        help='Weight decay (L2 loss on parameters).')
    parser.add_argument('--hidden', type=int, default=16,
                        help='Number of hidden units.')
    parser.add_argument('--dropout', type=float, default=0.5,
                        help='Dropout rate (1 - keep probability).')
    args = parser.parse_args()
    args.cuda = not args.no_cuda and torch.cuda.is_available()
    np.random.seed(args.seed)
    torch.manual_seed(args.seed)
    if args.cuda:
        torch.cuda.manual_seed(args.seed)


    print("read data")
    movies=np.load('fea_movie.npy');users=np.load('fea_user.npy');
    ratings =np.loadtxt('ratings.txt',dtype=np.int32)
    ratings[:, 2]=(ratings[:, 2].astype(np.float32))-1 ;
    user_mov = ratings[:, 0:2];
    timestp = ratings[:, 3];


    print("read gra")
    edges = np.loadtxt('g.txt',dtype=np.int32)
    edges = np.array((edges))
    adj=sp.coo_matrix((np.ones(edges.shape[0]),(edges[:,0]-1,edges[:,1]-1)),shape=(3883,3883),dtype=np.float32)
    adj = adj + adj.T.multiply(adj.T > adj) - adj.multiply(adj.T > adj)
    adj = normalize(adj + sp.eye(adj.shape[0]))
    adj = sparse_mx_to_torch_sparse_tensor(adj)


    x_train, x_test, y_train, y_test = train_test_split(user_mov, ratings, test_size=0.2, random_state=42)
    print("Train")
    model=train(adj,movies,users,x_train,y_train)

    torch.save(model, 'model2_2.pkl')
    y = Variable(torch.from_numpy(y_test), requires_grad=False);
    loss_fn = torch.nn.MSELoss(reduce=True, size_average=True)  # MSE损失
    xx=x_test;
    yy=y[:,2];yy=yy.float()/4;
    yy_pred = model.forward(adj,xx)
    loss = loss_fn(yy_pred.float(), yy.float())
    print(loss.data)



