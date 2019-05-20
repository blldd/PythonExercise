# -*- coding: utf-8 -*-
"""
@Time    : 2019/5/19 10:59 AM
@Author  : ddlee
@File    : code3.py
"""


class Solution:
    """
    5065. 最长字符串链  显示英文描述

    给出一个单词列表，其中每个单词都由小写英文字母组成。
    如果我们可以在 word1 的任何地方添加一个字母使其变成 word2，那么我们认为 word1 是 word2 的前身。
    例如，"abc" 是 "abac" 的前身。
    词链是单词 [word_1, word_2, ..., word_k] 组成的序列，k >= 1，
    其中 word_1 是 word_2 的前身，word_2 是 word_3 的前身，依此类推。
    从给定单词列表 words 中选择单词组成词链，返回词链的最长可能长度。

    示例：
    输入：["a","b","ba","bca","bda","bdca"]
    输出：4
    解释：最长单词链之一为 "a","ba","bda","bdca"。
    """

    def longestStrChain(self, words):
        words = sorted(words, key=lambda word: len(word))
        # words.sort(key=len)
        # print(words)
        max_diff = len(words[-1]) - len(words[0]) + 1
        # print(max_diff)

        l = len(words)
        if l < 2:
            return l

        def check(a, b):
            if len(b) == len(a) + 1:
                i, j = 0, 0
                dis_cnt = 0
                while i < len(a) and j < len(b):
                    if a[i] == b[j]:
                        i += 1
                        j += 1
                    else:
                        j += 1
                        dis_cnt += 1
                if dis_cnt <= 1:
                    return True
                return False
            else:
                return False

        dp = [1 for i in range(l)]
        for i in range(1, l):
            for idx in range(1, i + 1)[::-1]:
                if check(words[i - idx], words[i]):
                    dp[i] = max(dp[i], dp[i - idx] + 1)
                if dp[i] == max_diff:
                    return max_diff

        print(dp)
        return max(dp)


if __name__ == '__main__':
    # words = ["a", "b", "ba", "bca", "bda", "bdca"]
    words = ["theotmhxxxbwdrio", "dtngqeaxotylxgri", "alkssxodsowcmjlf", "gmhvmdjgiodmfajv", "siidklxmhtbayuzw",
             "sytkddlepdcthngm", "tunbxgxctlfgourm", "gllwqbqjjrrcphxs", "zifoeeehcflcmmuc", "smophvighbxeacdf",
             "fllmdrzumppjusxo", "huorokmwbcvovibw", "ixxtpfuymbalnosw", "riaybavlriotieop", "nsklwjnpddlkmtea",
             "zauybhhntmigdnuq", "vtjtdbguftbzfraj", "aovoadfzvmjmeyxb", "xpfhyjayrbzmvguq", "lunpammgzzwdcflx",
             "fwxfaklkezxcifnt", "jswjjlqoujopaxhu", "tlqkdtchusvytiub", "pwernqgrwypsshum", "qounndkwqmhoktzz",
             "rzjgfuoconquqzpl", "apiazrcusycrwiij", "bbrzggoolqobwvji", "shflgfshsgagsphh", "dujkwhssdpecjcmv",
             "looyhwjzcvvqznqc", "lihdntdziasanmra", "clbvdwzziuvaaruz", "vasoineuwqgkuqlg", "vzvewwcusmpbwicj",
             "bqanxzevllenbuqu", "hbdxrldgexagsntr", "npmlerlqvxwvybdc", "aphcqlqbkiuahjgk", "xuvneupnizoxivyb",
             "pjaxbcgvoontxkmr", "spzeirortbhitbne", "sckpxytqockyohdp", "labqyxlwthwomkah", "ycewaleyxtbuglme",
             "vpqczhkydnquxvao", "ytebgkfgxwjdxmqi", "sebtgnbjcgvpdxsw", "kstlanieyzfmyzfw", "shfnjqpncdtvgazt",
             "snisbkmjnibbzmeq", "qzubywdwtantumco", "fybipfyzbyalkmft", "qvqxcuailwufinvu", "kdnugvugcsaaotdh",
             "qehpwnrayefhmxsr", "gifwajkumqusatkz", "lamhxbhppqxwuvjq", "bwpokytivlcybmcs", "uvoburyztfohbdds",
             "ydrukcgaivdpitvu", "defbdujksrbkzfoa", "nubvmndazwehgdce", "wjthwpunersksmwp", "lgpowvxexmuluwlk",
             "lpfwwmeqvwytxgtf", "anoebptptckstaja", "qepvxxgvaqavtbaj", "zdwjycvckhxgczkt", "picdshtdrpcwmigw",
             "idxohsedigsuywze", "totzylcgfqgemlce", "eofunrijulusbzyh", "qdbouachrbxpeyjd", "nmrqqontsmzlrask",
             "bwwwblkrgvpbtedu", "cfdocehocejxcaqo", "cqvphiriibqanvur", "lejnxnlghnohyabx", "obcbnfrrfdwncztw",
             "wvhehrlecjmxmabq", "twcnfwjomnjjdkyd", "gksrnrazgzjjhuav", "hcwfmfvozthnkhxg", "lektsflpjszvocot",
             "hqgjczxujlfqlxqh", "okpubmdsgxxtgqqo", "oroaihxgcuamnkeg", "hczrogbfwpkdqjfl", "fpkcnbjuozyjvqwc",
             "yufwtijqgnfhwsbu", "ozowpddxcxggxspi", "dlzwufgwluswuxcz", "xpkgxkypbfttgpnd", "wpkyeoyninpszsti",
             "igteuhuncmrbcfeh", "uslmkvgbtgtiifzy", "tkiczlfkqaqomwnh", "eguryksflgmjgmcb", "scnjwzaigitfmvcl",
             "wwduzzrjcwdoshdb", "vmqevxshsooudbef", "ngvbmlvnsreapgjn", "xavbcnfalyjnqefk", "pbvivwnoxqttzjre",
             "wpmbnvmqsciufprw", "oyqmnhyiatjdnhqh", "omnzniialyeclkyz", "mzskeqtesowornrx", "gkimajgcecutywso",
             "sovngxfvmtkhugjw", "ugnjkhowbvhhqnbk", "bbwzmykefpdulevy", "vvgtuomeloqbvluh", "qrnzklgknmdnzruv",
             "hzshfeaafwqrdklk", "nulcalmpiadwbfrj", "irytohquphqlaspx", "mcmmunuudwdyglds", "bxyekdgpvcsordnv",
             "ujebecopmfuruter", "ewmxqyygmlbtikcn", "ifyszzvfzplxmfjj", "ltfypyahjmuwljct", "qbxwuirpjdxchiev",
             "bmcduqqzowznboiw", "eqmuffnlkvalhzav", "nrcmxwxdrytavxlw", "ujjfjtewfxwgjypy", "ezdscqpbgssmfend",
             "dguynrjcoqmwphwu", "bhlfccfvebykzbpc", "yjbfyzzziowlszkn", "hfkdkqautfnshnna", "eefmwametriidfat",
             "savvqdrurohusire", "wnbcterncfvuiwcz", "jqhylbusqkdslpis", "prentpwegnupueqc", "isarpecdscfsblmq",
             "uwusbjqzydgtbtmb", "wukckoceupegqobk", "fvvedfhaueivcdua", "unmqrqynisatinvi", "doiufbywbzhjatfy",
             "zfbypjjzfkvvvpdr", "iivadpzrtzzinfri", "lengrelvpztufodb", "yqbgezyadbondywx", "dkcjilykdgmerwmp",
             "pdqegvwikkhnzvrg", "kvpfqhxhnluqgdux", "dlnzgmunympzvddc", "hyxvyokkazbrzbys", "wijmhrfkrptskzlo",
             "izrpdwlzdzpbmjeu", "vpduyztdcqukrzjv", "ooxfwsqvhsbsnrwt", "ddkujqzlluvlfpsn", "wmldcdtfpriqtlpi",
             "kyecbanoutazaqbs", "uvaormkvpuixgppc", "ldmpnetrxqgqelcd", "ylhdtsxcdsnskcue", "wkecenpcstsmizow",
             "lftdjowraljqjjag", "pprelpevefaoucyb", "hiczsqeqzzlreakg", "hqfouzrylhjogyfl", "iweyqqblvqhjddkp",
             "euzjqijtnxphmhmj", "ogyogcpfykurtzaa", "soshkrxqzvfcqwcz", "ipdlwbpvgwrbnkws", "vyhxclemxnnnsuef",
             "qclhyijmbclledjh", "jawmwvvarkvzxqvw", "eouweepuygrphixi", "fesqehlapewyszum", "bwacsdseomnbsndf",
             "rsuuiupndusbnhkw", "dmivdksevuxkzjlc", "yogjkcciqhtudrih", "tanaomdzlbmaharv", "czvcedfffqbvheyh",
             "zvvngdvrfqokbehy", "nuqpuvmmxstcidok", "cyjvznquwbxflrrh", "fdlxjofdlssjwkom", "yhlckwyljirmxkby",
             "khozjinaoplnrbpo", "bhkpczxvycgbaplc", "yvmboqlqmvywbkfz", "gaqsoymdpouyuvdc", "nbchkpufkcxyeqxu",
             "xerboqanueassvni", "newqznpputrejnxq", "nuwasfnjgssdchow", "hrrxecchnltbqunb", "ltiudhomuwimtgee",
             "wgxrmrwjwvqaawwt", "nybuwobkophddowo", "iqgklkyknrnyhdhr", "mgradxxlqzsksnpa", "qetjinrxrbnbrmts",
             "mvcbqugryppfcepp", "ewxomaayewdwmwly", "gyocuoeauuvrnwid", "vubhmeeevbchhszz", "rzuuegbwrawfidlh",
             "didsydbettjuadft", "bodgnejksdruldiz", "pczglvplofnexttd", "fihlhusaqrwatbuf", "guhwcnnkojkzwqpx",
             "qklznhosfkjlewrp", "nflbxbbiiklstsle", "oigvsoqgtykkwmjx", "mmpocqhudimpyuun", "lecurvbutrofaucd",
             "jisxdceauwmkjikb", "hqinvongnqneurpw", "ycypatwybtxvnvxr", "vovxahrphtkxusqv", "cylnooyfaichacur",
             "ubhwrbrhkrnyxicc", "kzndvcprpgstjpql", "mtpjlgcmbxphxmai", "kjcoovphpyzrbgeq", "bqxmtcfjxuvmtesm",
             "nhxhutulonhipizr", "oyunexqvqxwrzjpa", "gexvujxodpyuglkr", "ixyuqlkrpuemlnwp", "aqeimvkhbbnuxtgv",
             "jlfzywmjfhhpgryq", "aexcykwgqydkmits", "ebhrghlxgrzeyhxp", "mwdvuynzwtghkawi", "pywcetjwgzmydhxk",
             "aivqqpzqniubbfca", "acnbattycbfowfok", "kinsnqvrsdkkgbor", "sfojdytnqycumwkp", "sqkfodmmadkscfmo",
             "kxnwyglxjgksopsl", "fyhqiidzasqyvxxv", "bebyobcpudxkzryp", "nqrcamzxlbkcdbfk", "lgiojggnvdtgujxb",
             "mrpxylswpdbxwflz", "iqgboadqunyywjly", "rmypapsdjpsudvus", "mjgrchwrsjrgfuco", "atwuxpebgcrbawzn",
             "fkqpxjtighxrfwmb", "uenyarzlxhqjmkim", "xrrtwdfavexnzmvy", "piiwofcijcspvykb", "nvvixstvfetbrdwr",
             "ojdlzgixtivthcya", "qqvfftrjlsgqmuvg", "xwcvevcpusywhvnu", "rjqeihcbhnvmsbnb", "chhxzgmzjnxjtutz",
             "fcokdwindmbodnvl", "uomtrsvpmafwptqa", "nvqqtfgozyhtkpxm", "dkhqtiavakhnxtsv", "luqfflxemcbwpxdx",
             "whrzozlyiworknmq", "kqoztcotvflsvrjo", "hygkslsfaiqogqqv", "bytzkefoaswpzecg", "bvkvshtufvtncfwg",
             "zykhqryqdflihtdl", "uqeozlxazimzfooi", "izupruozcvlflqud", "ynnrzflqktfvkatm", "bhlpawyywnmrjoiy",
             "yembxloeadhemgae", "pqqiaupwlsmvnztz", "tdjivdvcokkqdeyf", "iftopcdjkhgkukqv", "uinupdbbztjftlqz",
             "fdarvkdfqjyuzxxw", "ycjrpzfdiinhhatj", "dmkbuwikyhgdqdjq", "xlmynpcyornkxugr", "sxcshvtlphksdgru",
             "lfgkycfavtpfeivy", "oaterjnyeekraxhy", "sgebdjofrvpacdfz", "toksosabuxjagzfj", "yqilupmdpejjyywk",
             "qnzvhseerbshxmvz", "avwuljogxllumugl", "byncynqxsrvctjjt", "dxitrupbvplomfqt", "qxlhviwowwmidbrz",
             "ocgecpnudtqbllao", "nciuxqwlqruvukgb", "ukjxzdpqtnrmadrb", "jxdlbuihsqriydij", "dhwjuyflbbstsnde",
             "itajarjgmnauknqt", "uawzhjvkzeueiqhj", "aqshoatewzyxwyta", "dmisegqskrqdvfta", "fepndeorgxxkkabh",
             "khsbkzxagumpkiqq", "rgqtqummhrndvjle", "nievapfxczugccvn", "zhpfxskeomxqlgeg", "fijbzdueuvkhhswp",
             "ufaibxjnwhnaysou", "clnkdpcfyzioyezk", "wplkxfqdejrgguir", "jfgqvzilubftoeod", "fzohbnnbjczltvuf",
             "dgzlzwpfbdsrwxlt", "wscqassrxotgwvus", "qfdjmgptagtcdazr", "strmtgehrcfkwzka", "vxfjnupvwfrimtze",
             "ppoatjngnhxfiiua", "gpjyylzkvvpoeril", "dxabloqwvirgwsxn", "xhrnjedkgrfuzlhd", "znpxokjsvwdpkaen",
             "rxsygsieaqlcmwdm", "hkdxnsualmbidzpz", "byigghltxjmuckvl", "icbstomkfbpthxgk", "bwlamuxqrpxdgxrv",
             "etlcqssgzjilcspq", "fbomvubajirjgflq", "yjdlrvgxnqwsyrkc", "skqbbngaaxrcxbdc", "ykxkvocxzfxxxcbe",
             "fjeeehvgrnjsegzw", "oomtdojqhrhpspir", "aocbqqkolulwnmkw", "jupfmtqltzihfmot", "emzfcvbeodplybir",
             "tnhxetcmqnxanvuj", "hmtxxmraczeylbyc", "akxpizakgxnsfcsv", "hdnohyktzscatjvo", "pmeniqvhdnedwamp",
             "gzfsvjbinvifwbge", "ezkptosdjrxqcpkw", "vqqyfimkciueagjd", "wtkpwxodbyjidpfk", "saqrtwyurdtupmnj",
             "snqvbepqkeczmrbm", "htnleqnzzpzeosey", "ioiqamsryvdqdmzt", "vhpwmfjogjiajkji", "mlbxcihgsazvsjdm",
             "ierlwftnyidbbipl", "nelyjdhotyelodwx", "elicbdhueuwocmlt", "pdeiacbkdxyijuog", "ljickhhhgxerxdim",
             "rhiclfvjcncujxrr", "nsxqovmjiibsdzcs", "jlusuojscipzhetu", "xrrkdadafipdowfq", "gmpcfxitfkuwdceu",
             "aztorutiiuxstgch", "ztyouyucujxovodc", "oeffrqhhpazsrkgl", "eiksasymzuagxgxd", "evtwgamzsmohxjdl",
             "zphjzegvaqhcvwmv", "rbbqgxindxjpyclb", "wrqvbeeokewbinjz", "cxbzjlgfgyjycjwn", "sdeaefzkhydjgbub",
             "dhfnhufddkglfwxv", "xeauhzdfvbrmriss", "iycobiduvqemwtze", "cbbzsooyulxgcfke", "tiaipuzfjtdpxtzg",
             "incazlyudmqzdzrm", "gxeqptppjxffgrza", "zrplhypjscarepoa", "ejceebkxfbtifoyg", "uwhzrqkzgsgltruc",
             "epwiyilctktepyxd", "xiyukuftzzalhypn", "gksnvoqwbdgmqury", "fgxznnfgjgwaaohz", "kymalivbtmpzuhmh",
             "fxcwscnutndycinq", "djfirroowqbmfbwv", "mxygbjxrgamlauim", "zsffslybgiivieyu", "qlvntkojgbxabync",
             "dizastwughswkkfw", "cqhhbelsglqcpbje", "xqhduhittymnjion", "xvoupntxznsytose", "dcnhhkbvfvqvdxvd",
             "jpvyavuwlrngejwx", "oqujlaymjbfrbeuc", "sycvybsitlmquseh", "pamolxwmxgcsaswu", "oopuxzfmcghrfrww",
             "ceoelmfmfrlisiyk", "ejjphpcsnzjyoogc", "vgjbpmukjwothgme", "wybinspusuwllcff", "qjmyvmzkqyvjoeyw",
             "olfimhkyovlqbsvs", "spzpqsrtlyfwibrn", "ngsawsieyxnvbdml", "rhsjkestgccsfacj", "nvgohohfhwznucgz",
             "fyywflegaospsebl", "hbyitilgivftndoo", "beyrfiovcvpcfprn", "rhixjizbeuxidcht", "btspnuwqmmqmgmlw",
             "umarzpnzcpruvzjv", "hnnjhtcxsfoyzbwu", "qevofrbufcievtyi", "hlciqwiodzwqajjh", "fbumletwpopcancg",
             "ocacctvwzsdwjttd", "twwwdkeiadbghjum", "yhphxfjanwnbzpyo", "yaopcmwulbqcpplz", "tqbagnrrulenacrk",
             "wzhgkyropdqjcmrf", "xzlnoomepukznbli", "qeiwmxmlsvmovjok", "optnjnyyfnvykopn", "giuhspyhnbezdqus",
             "ikmqgsuqjmezhfql", "bgvzlexcubdvewik", "ldjqpzoaamimtrkw", "cauezhyyukshtgvu", "jbtbmcktglwpflvc",
             "sqaomqqdbciekdds", "mjzapaimbgqsrnmy", "pbiefytkyqleuqfd", "ojzfsgouujppxflm", "xmkvzkxotdxngwio",
             "edidnndoavhkhpee", "dnlxudtegjsmjspo", "lbohxchuikdaqwtj", "chuafnwaayplcgll", "nljyjztoviurpnas",
             "wfprmoouewnqfpky", "cfhbdkuliaratqqb", "usrbawmjnhairnjm", "lqhtvbglbvvxbmom", "gseclkrivgdtscxu",
             "ekxpqvksfeifdxto", "lpuknwsqvtbeirdh", "frynisnarflxvcma", "irfodtprcfkxrsfd", "ssejxdljecjdvfhu",
             "ttmgowtpfumrdhzw", "wkfnufnbebkmkalj", "tvgsmeudsqkneuzo", "rnvlhubwpuslqpez", "jehdwwemxzrveqio",
             "ifbiujmfrurhmabo", "xryqpcljgsmttbao", "tfmgztbudtkxdvxp", "icooabpevxwfbfhy", "jmigzogrrkwjoeaz",
             "abuepspwmkqhfrbn", "lrrsjfmecfuaizkw", "iyyreqwsoqrwxacm", "vpwbwohkmkyrjhpv", "vwtyqxbtdbakkiek",
             "ogyxhzjyqnhdrqhj", "awlfbyutfzmeqgas", "itleasdcvufjssct", "ujqsbjwbrvysypie", "pxpxifbutjkvgwny",
             "paugmvbkhbvfrjpt", "mwptdslorcclbnlo", "jsnbtptjlaamnbcc", "jkqmtkiupljyxvyq", "wnnsswvrtqobpoji",
             "lukkgekrbrgcuuvg", "myvkxbjlkkjbbviz", "mspgrhgyrslmvgvb", "uxjwimagbtmeozle", "yzbyhuupbfgtpfie",
             "jjpxncnqivjwnwzi", "zsfmbiptskzkdmrz", "pybokowpxtkuupap", "umtvlacagjydqocz", "vubbhnibeyfofktm",
             "untyadrbmvtdpgik", "omrwgpjnbghcjgrg", "jqudvapsvdzcepzd", "jttppcltqmdqbxag", "dsruyscjggxsflbh",
             "qaedohbuijwfgfsf", "fcwmtfhsaagtphxq", "xtjqcwdhqtokwrwu", "finpmpbvubclpkbu", "kjrofivigxglbpzj",
             "xbiyelrnijwrbwiz", "tbollwoehjyqybmy", "nyonyivvgthokgwc", "dnmtbglqtwdfeybj", "sexmgatxlqwwovqj",
             "ygdnwddelvphxsqx", "xrqlqkfscljvpmmx", "uwyjegwbmcswbedq", "gpqpnuyhtibqthrm", "jbitmxzkydqqqnam",
             "qelsowbtoyenucrj", "izawtffapryazkel", "ahhxbnipiqwztqfp", "bqcuindmcukdidsk", "fyuqndaddunlncic",
             "qrqddpddsugmxplm", "sjhkguvbmmwbzkwk", "ntynhvmsufztqmny", "mgblnftagevlqtnb", "mzyjcwbkvabvpedu",
             "yeacmasvtcntzpbm", "yyoicmseymivorzk", "zgyfkavgudjhcavo", "zwsrpadzepqaosah", "wagtkxbfkgmrwdfe",
             "crnslxwtvwhldbsl", "wgqmjoeclvfqvwis", "cankxlbnygrffbxn", "hdtoyqqqtdmxjiog", "eaewhgtkgojyeswf",
             "giffpypjuhmaoipi", "hggslwymnpmuuwob", "ottepjsncvkdjygg", "pbeuxnhlsqngtoka", "zkmmxacxronxwquf",
             "gzscuunoccyupoib", "cuovmowpaxtpripe", "bywxbqvjdctmesht", "phwmjltmhujbwrrh", "xvuqknirmcnxqoll",
             "fpgxjcswecpigkhs", "rvsbzfammkwbozvu", "wtxqutjjkjpknump", "ocohmyxhgvfuedeg", "lrdgealrblcfoijk",
             "rngvutxhlqxodvaw", "jvlxpgdixaacqnvp", "rooamxasghsxbpgk", "palbfmdpppvmrppt", "mlvwnripsuxswpad",
             "tnoupdwcuadwqmzp", "jpcltrwmniuyvydg", "vlufcqyxojmcyimw", "itgqahyhbsavqmlv", "smatgazvbscwxspt",
             "tvbshaztzoursrbp", "mtpljtszeuloekac", "xlrrwokrihdarwmy", "kzhwhbfbzpewwglp", "fnzecjkgxdhwrhah",
             "ultxhoflruibgktj", "rhhrvrtvayfvjlbl", "vfhayzhkupiqdpei", "vzrwwuqdhpsbkefv", "eymfdfctsxlhiuux",
             "dclflrfemieynfig", "uanduhitodbpvlzw", "mcoykzynhyeasvoa", "rwzqmsejmestsxsp", "zmdlyshufmumuhsb",
             "pjqfggkhyoyiwqkr", "veuwzmohpjgvbsrf", "hfagungunkgeozky", "tdibggojyycyifai", "iszhscwzncsvsnjj",
             "sqhmlsoxficuqbmv", "bvsgbcvnraaclpef", "ajdmvjjbulznzhdh", "dmqjkcvlzvmouxnu", "ntstwpjpycqgxxhw",
             "teellkcqwfgjpazg", "zwpkvhswzatiftbe", "ezhjuxswvclcgtbl", "nrpventzfcfyeojp", "lpfbcjpgsndbxtjb",
             "tffcdsqthnuvnpjb", "znfrikbdvnqztgtl", "eepefgkvxjobjgpj", "lfnfkolohmnuuqvh", "xaillgpzkwtuxhew",
             "esyvqqczdptqbagr", "fhunclqpehwhdauj", "kamecpykuabvajpe", "vysrpkiztasdtsrn", "sydzfecfhazmhqhz",
             "yjldwljpiesdtfyw", "ijnninczrctinrvn", "bckazagjaaqevijy", "yaazidyuaniohwej", "iacnekknhkbwhkrm",
             "twwowrgbwmncaika", "fkadizmtgqujccop", "xsewwwxxktwuaiqp", "benszqzmvrxvbqkm", "xidbqnwoxjpzelbn",
             "qwhjuhmbnqlbhcsa", "clbixbphfndiaepu", "qchgfxpoxvvfopjm", "iwevfsjtjynlpjbc", "hvecyccirwdlqpng",
             "vckdduhuosomoekp", "pxoksilhvmpdhpma", "jtpxvipeenmkkafd", "ouphnwggncyrlicr", "yfhsxehxrcqlnbfc",
             "yvyjopotalqevayp", "tkzxpwunwvrbatkk", "dncppzicvahvueyg", "wnzhovbfxvqehxuf", "bppwgrlsivokozbo",
             "uhyojwbhwbqutkvb", "hlzdlfbtcbdsfmzq", "zanszwktvoniazpl", "vkxbdfpxsiubrgxp", "obdsftaogqgegnvl",
             "iyxhqdmescoyvzva", "hdfhogjcyppkdwek", "hdhsjfejaocclmfj", "ogzwgoshnfftsnni", "rispfgsnnmdbwknj",
             "kslqrbzswjowsufn", "unazstbgggmjjaaa", "lkdrstpexaligmjf", "mjyftuwhkqeludlu", "trrndsmsbylbmpdv",
             "ikmombgpdpgwijtq", "rwwkcmofbytcveph", "mplyjuoyqluflqoe", "xgbrstksxcezkrkf", "ofppuyyjmrdrbkdv",
             "ybketfvaltfazlvp", "psbbcbzjzskictps", "hyrztnnqnlvcxlma", "uujbpawcqlfnvwda", "ecstieumnhisyavd",
             "mjhykxdswlclikmc", "xjpycnttepqlxgma", "pfsykmvzwheycwrr", "haofsesgkiiislze", "fleabsqfpspdwkdx",
             "vddrrffqrcmcxijt", "kbdkubveqjqktmne", "trqqztjkajjzgwfx", "tuzttdxqffwnltyn", "wxmthzndzweyackl",
             "azuhgzgneqwpumow", "qhirpqvmnmvxeeui", "xuoqrywjatlagqmc", "cpylzwcogppdnlfk", "nqqiordouqxysneq",
             "cpcymppjrsidyjwz", "izxljjxpbmuhtrwb", "xsclfdqwmthocsrz", "jlugnlflzhdqkizv", "hcheppgxzujiockx",
             "ghvbhmpwqgqkhglc", "fjmyuhqgesljphon", "qoyjwfpbxlfcvcxp", "tuumxdfhyrvlxjle", "wvwnmbvsdreswvda",
             "zegpobltcdwwxzgp", "qnkogfgfslqfycet", "ghgchveecjrmrxpj", "ghovhsgxckkxzkyc", "xtujujibyfrxwabf",
             "jbyhjkxzlotaecsy", "ziyytxebtinmwcwx", "gdvbzrbiquwagxbg", "jjkkysyiiubtapzp", "ascckcngqygqkaov",
             "zkjleqhguxwgexsk", "ydpupehhlnrphzjx", "awbahrkehbcbeore", "fhdhfmndtcshceoo", "vmchkjuzygqyqbpv",
             "ibiuejuupgexwfip", "zetvewqagsltquga", "dpsfalwyhhcxstyq", "peddrszjyuqvkjmr", "mcfrvecxiapqsxzy",
             "ctlebqmhwqxpnpno", "rksiqmlwbgzuaxxm", "tyelmxihnmtwqexv", "hiawgmiztbjriycu", "zhtwbablrvegmntv",
             "ihpxwvtohcqmrpbp", "deofexcffyisbstm", "phaevnhvgzqxillc", "anxzzuszfcemdzhd", "rnktkfljduzxoviq",
             "pucqeejyzordgoen", "rjyjojrnouysjfzb", "zhluavvvzgigcypr", "bttdbdmvwunjzcmo", "kicbmwiglrwbeuin",
             "vecndshiaothpobi", "kbdhxpujyqxaipkk", "yrxfanwxykpgayex", "fexzfmohmalzxdaa", "krlfemruoxqyaalu",
             "wodznukscrnnsxln", "hocgollnfbunnkmc", "vspgthxatoqgfvfi", "zsiacjiymcwmsefg", "uxhkpmpyijxekjbn",
             "fuonhkuolvfabusw", "dnoinqeohkmxctrc", "ygqppdjuotwvayef", "bglmvggbqhsyonas", "dkibofxaekhkjcnd",
             "wnihowwtffrmcthd", "nksepcspmteignox", "hmetkddmndtmgytq", "jdmepfhfiezgxgrv", "qlzyojbxtloxxqgg",
             "pleawbetmnqmtqwv", "fvittukpegmccdvb", "fijvwcfnieoieesu", "eulddkchrrnovtxo", "qtubxwqossmwyvgs",
             "rgqansjdqcbvftah", "hgnalrxlqcvgmeaw", "usyflznkjbdablvv", "lbotyzydzbpouwbx", "otvbrpssoafyaran",
             "udzdmcwobdtonvpp", "phmyhisduwicernd", "yrmviugmjmsecqfj", "fuilitbprekpbzts", "mqcealippibzydfo",
             "kzddfaxbcczgwxkk", "brzbgqptwfgagvln", "iuqqagrcenldaodq", "xmdradsvbxzpqobw", "ijvbtdaauvhxmyzo",
             "gzesmxjjtuyclznv", "rtjvvjoudjtigkfa", "fbhzohpgiwbiggou", "eqribgwnmfzsdjyg", "daqgpdnghejvqyer",
             "htcnsswneohxzelg", "nmqfqlkwxerlxnoj", "iblbnigfawxwxidl", "zzhomcrbvvdhhgis", "chktjjazdlryuxbn",
             "erlxbegtsfyweile", "kuqqnuyzkljtjsaj", "isdlficxpyodacic", "aifpqykqfiqtqumj", "kmegszbxmrjfajxo",
             "hkvbxntzjnkgqutu", "hgwkazdqcdowfcci", "emecubruaxxfwuqq", "vuflprqqyybhllel", "ghixpkuubmzwcpdy",
             "jglryeozxyzxhacx", "jccxefyjkuftkiaa", "blvtdwivtfpkovpr", "bripodntdlclxdnt", "wkayvgdktndvvrrp",
             "izdysvxwcsmsvrha", "wowloiumbacceurr", "oxbzugcqqwdwseiq", "cgqbgjsedyadgjlv", "okyyvnmjyvdklkrl",
             "ixsdvhfedbtussgo", "ttmgmmgnfgsuzkrj", "ozreyjyqeljbsekd", "unzmhfgnjvvhojev", "goynwpxvlsilcrbt",
             "isdynbjwdmovczwd", "dmfdrlyayuhmmuuu", "gcnkbotxlrcedjnm", "lrkikxsjqqgejqkd", "glkazvjicilefypt",
             "iapavsnwcfilgcno", "bxtykhdqbabagvlo", "xmjwpoqfhxkxtruk", "lzliajiugmevkjly", "pwbedxrfmjltlrqz",
             "srzxlwmtfculzsom", "xrehgbkrmamrisxp", "wfpavvcomhljsvpo", "ghfhcxnzetmruxrh", "mvvpljewvojhuztz",
             "jesommrnwhvgwrcf", "clpcltpawljpmjtd", "wtfarmgwbhybzljm", "boopukijtyxjpptg", "fkexhohrmpldfqpp",
             "aojwipwghfmaxxvg", "qrbgkiamhklmpqls", "hbuwrahiuicimgtq", "uezvtdiejuretqpt", "soormkhajtlmuzlb",
             "ukgwsnigurlzovmt", "ihyfroiasrpqsvbi", "swashgeensjojhay", "yuryjbqjimpbrskn", "iqpozpwxvnxzzawj",
             "xaidfunanyfnpkuq", "vgcgowmnyrqefblx", "iznwchridsphoyud", "lypcxyakmzgottlp", "artkgkrmmwnmzvgl",
             "zafpvffrfsangdsb", "ueyqfpkpqieqaafh", "baocbzajmnidtnwq", "gkprixqzdfblwpxl", "hhjfizfieopshkwm",
             "nrceegdamnfewooe", "cnomggcsmciynypk", "kcqxezjyjblgjnop", "qrmgdvhemsgaffrf", "yogcyfqqtzyuasml",
             "fzhxlrpuvhypoggy", "twzbkdaksmaoumjf", "aqsqzfbzgwnwdrwj", "fvgulzwsughjpazw", "gjofslnrajoetxxp",
             "cdhvmnsrlefrgrle", "tnucutlmfcteyvzb", "iglpmzviyhyqazvh", "ulxtqqlnqlfwmcux", "xynxelruqaouhifv",
             "vqfcjjkdmrrfrpdt", "xyapannqicvkwvvg", "alzqxgouoajfpznm", "uxjilgikoqqqjrmy", "nxmrdlijvkwdkolp",
             "ieurtyvxomdkzfsr", "gtrgjjxcctuphtfd", "xqugpibjlgfcykei", "noyeddeuzbsuaovz", "vcyagbgqwpnqjurr",
             "mgucxxvzrinaoctl", "ihcxsxbnydicytcl", "tfewazeyvbbsyzts", "dmyjkfmbeanovqtg", "ojmpfixsbsikfjbw",
             "zgljdpldorogwyvc", "oqreqhloaqiogban", "ukrhmccbubuvzgva", "fqrvfhtpxdbutfoc", "ffgdoplvntuixroi",
             "nocjkhurwywnoocq", "ceseettdaidkfpgk", "tgdnfvboqdxalekk", "qbvwjnfwswjmddnp", "pqgarnhaofrweins",
             "fybfcmgelrvkqnav", "aeinpqnzozglctrv", "wvkbpygsjbtnyyyr", "bnkjlqkxhciuzgli", "lyxnihjhjmxgcgad",
             "doqxstyarcavfapp", "ojjpsxxivcrdzpof", "itzunfjdmidumnnk", "cnxczcsdlbqsgieo", "hgcmfpugyoyiuvrr",
             "nmlbwedkkiomtahi", "unkxbydwhgnrpaqo", "cvhawbjtpozgxttn", "nkipguegbesvdhgl", "hpfhibqhoqtxgwdg",
             "qjdfirmcukvdgswj", "yaayicraeufsoppn", "vgjzviemxjurvmqg", "udlzhgupsvsxzzfg", "fkkrdalgnqommwau",
             "tvhscqdotorjdaoe", "mpuzrydtmgylzkcf", "cdhtuovsueuyfmjd", "yyqaevempxviqdva", "ehyxexnbypoeugbu",
             "uwtvvbziulwbqlby", "lljehaxmhvwyvbat", "ccmglhmvavyvozzj", "lrkdvciahtmoqiof", "ieftsaioawvswqqv",
             "ijnamrbbanxpgffi", "xzvkvtpecitkmzht", "jqmfzimlkyqxraxo", "tmrolyeciwysmyop", "zxrdlifzpbfyvgpm",
             "psihysegxklkssgm", "gpjyjzivlxzhybjv", "poxdzcyqsdtjfcni", "qwrjbeveamhfrunu", "lpppcvfbslcqocxu",
             "yztickgnyexgqyra", "vovkykpscvzyhfdw", "jtdyyleejfavraax", "qehgqihbcdidwozr", "gdpaezpzcvmbtgpe",
             "nnwrftagsbxcnrtz", "vriauokmicjbkhsi", "ehqmchcfqzjpqajn", "fdxbpeaawtjukuaa", "dunhdxtwjeyzlibx",
             "anlgttoegozolamp", "qewjglziaveeiszg", "emfssiquhcuqkhje", "lrwkygcccbzdzyqt", "loobcpyybqpuibpt",
             "fwaaeyglghhpynya", "gjayiryyzugkscxl", "hctekocopsqfibai", "pzldhzazkmkbiwln", "okjsispxyzclnxkx",
             "svfegygnqnfpqjbj", "eedxrlejefgquvkk", "jdmckidcygyhwbjw", "moutzhyllumsapje", "npmkqywtitfywsle",
             "eaqcfcyazhdsrphc", "oltyffxxiwvykyvh", "gheuabmujfgystnx", "ecahzcxeeqleuqnp", "ejtlrtbcgpgkaxfg",
             "ogskgilastwjyrkw", "lbqtntnxgkvfpfdy", "pkxbrseiriqtnwqt", "eooaaieqwgyzscjo", "ibzbhsjtfcefzlwn",
             "skmzltizvbigduav", "vkvfjohjbcslgvwc", "yvlnvanyxvhoxzpu", "uxyeeubozejyxbib", "xdfcfzvqmtxmyxgx",
             "quaouiucehxvgnug", "teqaovhphsohvnrw", "hjgrfyrlgdciqksk", "valxfzeqkiokvzqf", "iqwzeygqklzcsoee",
             "esfcocbrkacqkuim", "bfoooiyczxlkmptf", "iocbwbjpkgihawru", "fyovgxsuligmazii", "fyceelkcpgemlcie",
             "wmvewcpgoqxueiyr", "ysjrpiepkqcmnbke", "hdornlieclgiqzko", "qfljqfjqfqsvlmxd", "khdfndtgvmuxpbfw",
             "dzkasverryenzfqx", "wimcvikfpcukuzno", "cokolqegtchtzcbo", "ebircudlmlguyceq", "dtfeveovxoppsexh",
             "apazjbuavofknubg", "kkezaiuvkyxbqihp", "szfvidrpolmtzfpd", "bubngeufukzekotv", "mjhwzotqfyxepypf",
             "dvykzwidscykpmaf", "ucybkqnkvmgwqjrf", "zzixagdoexsqabvq", "nqglwuqgjwqgjxjv", "ojisrhtrjogumpoj",
             "tlnxbgznjftwacsh", "uutzyqupsadzvddw", "ttrxgkujiusmegeh", "oappwmwnlouwokbs", "bcynrsajjghvjhyx",
             "fwfqurnipykrafzr", "dzpnbysdtooqkqse", "gnaxjtrmjebpxxrt", "rolnbsvmdgkbbzew", "tknlcmhdiaktrkxn",
             "kzdpwucxkecocsbp", "agjagdnkcaxrqohz", "rltzsszchrmdbyrq", "nenkbwrrseysuvpp", "fcrkvefgqruhpmeh",
             "azymauxmydlzdxhz", "ersrbrdjozxdpyds", "ohpjlblrkpgcnask", "coelsgildxhmqceh", "sxcjgfrvgruciuge"]
    print(Solution().longestStrChain(words))
    # print(Solution().check("ks", "kass"))
