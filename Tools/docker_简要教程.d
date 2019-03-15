1. 创建 container
docker run --name deploy -v /home/jianxiang/downloads:/root/downloads -it -d hunter_ubuntu
-d --restart=always 意味着无论容器因何种原因退出（包括正常退出），就立即重启。该参数的形式还可以是 --restart=on-failure:3，意思是如果启动进程退出代码非0，则重启容器，最多重启3次。

2. 进入创建的container
	a. 查看创建的container的id： {Container ID}
		docker ps
		// 4049c7fa0668

	b. 进入container：
		docker exec -it {Container ID} /bin/bash

		e.g.docker exec -it 5f785cac00df /bin/zsh   (你可以用/bin/bash，但是个人感觉/bin/zsh比较好用)
		9346da569f2c
		13fabb1dd484
		3f37e11de28f
		234908fe7ef5
		5f785cac00df

	c. 退出
		ctrl + d 

3. 在container里，你可以安装项目必要的软件，把项目的代码放进来等操作.
	a. 复制
		docker cp /etc/profile.d 4049c7fa0668:/etc/  
		docker cp /home/jianxiang/tools/apache-tomcat-8.5.16.tar.gz 4049c7fa0668:/root/downloads
		docker cp /home/jianxiang/downloads/mysql-5.6.26-linux-glibc2.5-x86_64.tar.gz 863a57658531:/root/downloads
		docker cp /home/jianxiang/data/word2vec/wiki.zhs.300.bin.gz 863a57658531:/root/downloads
		docker cp /home/jianxiang/downloads/customs.war 863a57658531:/root/downloads
		tar -zcvf customs_flask_test.tar.gz /home/jianxiang/pycharmSpace/customs_flask_test
		docker cp /home/jianxiang/pycharmSpace/customs_flask_test.tar.gz 863a57658531:/root/downloads
		docker cp /home/jianxiang/downloads/instantclient-basic-linux.x64-12.2.0.1.0.zip 4112582e4239:/u01/downloads
		
		docker cp /home/jianxiang/tools/svm_rank/svm_rank_classify  863a57658531:/root/tools/svm_rank/
		docker cp /home/mengxiao/tools/liblinear-multicore-2.11-1  863a57658531:/root/tools/
		
		tar zxvf /root/downloads/apache-tomcat-8.5.16.tar.gz -C /usr/java/tomcat
		tar zxvf /root/downloads/mysql-5.6.26-linux-glibc2.5-x86_64.tar.gz -C /usr/local/
		tar zxcf /root/downloads/customs_flask_test.tar.gz -C /root/pycharmSpace/
		
		
		export JAVA_HOME=/usr/java/jdk/jdk1.8.0_40/
		export JRE_HOME=/usr/java/jdk/jdk1.8.0_40/jre

		docker cp 863a57658531:/root/pycharmSpace/customs_flask_test /home/jianxiang/customs_code


4. 提交在container里修改：

	docker commit -m "message" {Container ID} {reporitory}:{tag}
	e.g.docker commit -m "anaconda2" 9b5660dc83c5 hunter_ubuntu:latest
	docker commit -m "jdk" 4049c7fa0668 hunter_ubuntu:latest
	docker commit -m "tomcat" 4049c7fa0668 hunter_ubuntu:latest
	docker commit -m "addfile" 863a57658531 hunter_ubuntu_port:latest
	docker commit -m "flask" 863a57658531 hunter_ubuntu_port:latest
	docker commit -m "running" 863a57658531 hunter_ubuntu_port:latest
	docker commit -m "newest" 66f085c3003d hunter_ubuntu_new:latest

5. 查看提交历史
	
	docker history {Image}
	e.g.docker history hunter_ubuntu_tz
	
6. 删除
	删除镜像
	docker rmi {IMAGE ID}
	docker rmi $(docker images --filter "dangling=true" -q --no-trunc)	
	删除容器
	docker rm -v $(docker ps -aq -f status=exited)      批量删除所有已经退出的容器

7. save & load
	docker save [OPTIONS] IMAGE [IMAGE...]
	e.g.	docker save busybox > busybox.tar
	docker save hunter_ubuntu_new > hunter_ubuntu_new.tar
	ls -sh hunter_ubuntu_new.tar
	
	docker load<hunter_ubuntu_new.tar

8. 查看镜像
	docker images
	
	
一般情况下是不可以改变容器的端口映射的，只有通过run命令指定。
如果想要不改变容器内容和配置的情况下更改端口映射只有先停止，然后将容器打包成镜像，然后在运行新的镜像的时候指定新的端口映射。

#先停止容器
docker stop containerA
e.g.	docker stop 0a9600038d4c
#将容器commit成为一个镜像
docker commit containerA  newImageB
e.g.	docker commit 9346da569f2c hunter_ubuntu_tz
docker commit 863a57658531 hunter_ubuntu_new
docker commit 13fabb1dd484 hunter_ubuntu_cp
docker commit 234908fe7ef5 hunter_ubuntu_oracle


#运行容器
docker run -p <host_port1>:<container_port1> -p <host_port2>:<container_port2>
e.g.	docker run -p 8080:8080 -p 8081:8081 -v /home/data/:/home/data/ -dt newImageB
docker run -p 8080:8080 -p 5000:5000 -p 9001:9001 -v /home/jianxiang/downloads:/root/downloads -dt hunter_ubuntu_port
docker run -p 8080:8080 -p 5000:5000 -p 9001:9001 -v /home/jianxiang/downloads:/root/downloads -v /home/jianxiang/customs_code:/root/customs_code --net=host -e TZ='Asia/Shanghai' -it -d hunter_ubuntu_tz
docker run -p 8080:8080 -p 5000:5000 -p 9001:9001 -v /home/jianxiang/downloads:/root/downloads -v /home/jianxiang/customs_code:/root/customs_code --net=host -e TZ='Asia/Shanghai' -it -d hunter_ubuntu_oracle

docker exec -it 9346da569f2c ip addr
docker cp /etc/localtime 13fabb1dd484:/etc/localtime


container 里面，你安装各种必要的组件，然后commit为一个image，到时候save出来一个文件；数据+代码另放
可以整理好一个目录，里面专门放我们的代码
data-packed volume container 其原理是将数据打包到镜像中，然后通过 docker managed volume 共享。


du -h --max-depth=1
ssh -X jianxiang@precision
df命令是linux系统以磁盘分区为单位查看文件系统，可以加上参数查看磁盘剩余空间信息，命令格式：
df -hl


SET PASSWORD FOR 'root'@'localhost' = PASSWORD('passw0rd');
cp libgomp.so.1 /usr/loca/lib/

apt-get install make g++

ln -fs /usr/local/mysql/bin/mysql mysql

apt-get -y install language-pack-zh-hans
export LANG=zh_CN.UTF-8
export LANGUAGE=zh_CN:zh:en_US:en
export LC_ALL=zh_CN.UTF-8

ALTER DATABASE customs CHARACTER SET utf8 COLLATE utf8_general_ci;
ALTER TABLE  doubt  CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;
ALTER TABLE  nameDict CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;
ALTER TABLE  new_predict_201807 CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;
ALTER TABLE  predict CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;
ALTER TABLE  rule CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;
ALTER TABLE  stopDict CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;
ALTER TABLE  stopNaDict CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;
ALTER TABLE  stopTyDict CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;
ALTER TABLE  synonym CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;
ALTER TABLE  task CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;
ALTER TABLE  typeDict CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;
ALTER TABLE  user CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;


/usr/java/tomcat/apache-tomcat-8.5.16/webapps/ROOT/WEB-INF/classes/customsIndexNoTokenizeNoDupSmartChinese
original.no.tokenize.no.dup.tsv

 cd /home/u01/Downloads
 unzip -o /root/downloads/linux.zseries64_11gR2_database_2of2.zip -d /home/u01/Downloads
 linux.zseries64_11gR2_database_2of2.zip
 ./runInstaller -jreloc /usr/java/jdk/jdk1.8.0_40/jre
 
 
 ---------------------------------------------docker oracle----------------32bit------------------------
 docker pull sath89/oracle-12c
 docker run -d -p 8080:8080 -p 1521:1521 sath89/oracle-12c
 docker run -d -p 8080:8080 -p 1521:1521 -v /my/oracle/data:/u01/app/oracle sath89/oracle-12c
 docker run -d -p 8080:8080 -p 1521:1521 -v /my/oracle/data:/u01/app/oracle -e DBCA_TOTAL_MEMORY=1024 sath89/oracle-12c
 docker run -d -p 8087:8080 -p 8021:1521 -v /home/jianxiang/pycharmSpace:/u01/app/oracle sath89/oracle-12c

 docker logs -f 4112582e423992291a9c9d93ad511f7256a1eebe124eb87b38b96c8730550b11
 docker exec -it 4112582e4239 /bin/bash
 netstat -nlpt
 su oracle
 cd $ORACLE_HOME 
 bin/sqlplus / as sysdba
 select database_status from v$instance;
 ctrl + d
 exit
 exit
 curl -v localhost:8087/apex
 curl -v localhost:8087/apex/apex
 
import cx_Oracle
conn = cx_Oracle.connect('system/oracle@49.52.10.181:8021/xe')
conn.close()
---------------------------------------------oracle 64bit------------------------
mkdir -p /opt/oracle
cd /opt/oracle
unzip /u01/downloads/instantclient-basic-linux.x64-12.2.0.1.0.zip
sudo apt-get install libaio1
vi ~/.zshrc
    export LD_LIBRARY_PATH=/opt/oracle/instantclient_12_2:$LD_LIBRARY_PATH
:wq
source ~/.zshrc

apt-get  update

docker exec -it 0a9600038d4c /bin/bash

docker cp /home/jianxiang/downloads/get-pip.py 4112582e4239:/home/oracle
----------------------------------------------rhel7.4------------------------------------------
docker search rhel7.4
docker pull u998/rhel7.4
docker run -it -d u998/rhel7.4
22e75889c87d
docker exec -it 22e75889c87d /bin/bash

sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo

CREATE DATABASE customs[CONTROLFILE REUSE][LOGFILE[GROUP 整数]<文件说明>,…][MAXLOGFILES整数]    [MAXLOGMEMBERS整数][MAXLOGHISTORY整数][DATAFILE<文件说明>,…][MAXDATAFILES整数][MAXINSTANCES整数][ARCHIVELOG][CHARACTER SET字符集名][EXCLUSIVE]
CREATE DATABASE customs CONTROLFILE REUSE LOGFILE GROUP 1 (‘diskb:log1.log’,’diskc:log1.log’) SIZE 50K, GROUP 2 (‘diskb:log2.log’.’diskc:log2.log’) SIZE 50K MAXLOGFILES 5 MAXLOGHISTORY 100 DATAFILE’diska:dbone.dat’SIZE 2M MAXDATAFILES 10 MAXINSTANCES 2 ARCHIVELOG EXCLUSIVE　
select * from (select t.*,rownum ro from (select id,createTime,fileName,predictTable, EVENT_ID from task order by createTime DESC) t where rownum <= 10 ) where ro>0


-- Create sequence 
create sequence SEQ_NEW_PREDICT_201809
minvalue 1    -- 最小值=1
maxvalue 999999999999999999999999999  -- 指定最大值 
-- 或nomaxvalue      -- 没有最大值
-- NOCYCLE;      -- 不循环
start with 1   -- 从1开始
increment by 1  -- 每次递增1
cache 20;
 
--触发器
create or replace trigger TRI_NEW_PREDICT_201809
  before insert on NEW_PREDICT_201809  
REFERENCING OLD AS "OLD" NEW AS "NEW" FOR EACH ROW
begin
    SELECT SEQ_NEW_PREDICT_201809.NEXTVAL INTO :NEW.ID FROM DUAL;
end;

    "select * from (select t.*,rownum ro from (select ID, "createTime", EVENT_ID, INSTANCE_ID, "queryName", "querySpec", "queryProductID", CONFIDENCE, "predProductID", "candidateName", "candidateNote", "candidateSpec" from new_predict_201809 WHERE 1=1 and event_id = '1536386715134' and ((queryProductID != predProductID and confidence >= 0.5000) or confidence < 0.0010) order by confidence DESC) t where rownum <= 10 ) where ro>0"
select * from (select t.*,rownum ro from (select ID, "createTime", EVENT_ID, INSTANCE_ID, "queryName", "querySpec", "queryProductID", CONFIDENCE, "predProductID", "candidateName", "candidateNote", "candidateSpec" from new_predict_201809  WHERE 1=1 and event_id = '1536386715134' and ((queryProductID != predProductID and confidence >= 0.5000) or confidence < 0.0010) order by confidence desc ) t where rownum <= 10 ) where ro>0

	