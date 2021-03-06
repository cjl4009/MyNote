#coding=utf-8

from itertools import chain

import jieba
# 导入jieba中的词性标注工具包
import jieba.posseg as poseg
import matplotlib.pyplot as plt

# 获取形容词的列表函数
def get_a_list(text):
    # 使用jieba的词性标注方法来切分文本，获得两个熟悉word，flag
    # 利用flag属性去判断一个词汇是否是形容词
    r = []
    for g in poseg.lcut(text):
        if g.flag == "a":
            r.append(g.word)
    return r

# 导入绘制词云的工具包
from wordcloud import WordCloud

def get_word_cloud(keywords_list):
    # 实例化绘制词云的类，其中参数font_oath是字体路径，为了能够显示中文
    # max_words指词云图像最多显示多少个词，background_color为背景颜色
    wordcloud = WordCloud(font_path="SimHei.ttf", max_words=100, background_color="white")
    # 将传入的列表转化成词云生成器需要的字符串形式，应为词云对象的参数要求是字符串类型
    keywords_string = " ".join(keywords_list)
    # 生成词云
    wordcloud.generate(keywords_string)

    # 绘制图像并显示
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()

if __name__ == '__main__':
    text = """近日，谍战剧《叛逆者》在央视八套播出后，就迅速成为人们热议的话题，有网友说：“从朱一龙官宣《叛逆者》开拍的那一天起，就在期待这部剧了，民国、谍战、人性、成长、情殇、叛逆、抉择……看点满满。今天开播，果然不负期待！”还有网友说：“很久没有看谍战剧了，一直很喜欢这类题材，看了一集，节奏紧凑，不错喜欢！”更有网友说：“不错不错，情节逻辑严密，人物真实生动，一点也没有虚的假的糊弄人的。”甚至有网友评论道：“一个文艺作品最核心的就是故事和讲故事的能力，果然李晓明老师不愧是你。这个故事结构，故事脉络，故事逻辑真的太舒服了，而且叙事节奏很好，把这么大的信息量安排的妥妥贴贴，追起剧来真的很爽！”

    现在《叛逆者》上线4天，VIP已经可以看到第10集，仍然保持着开播时好评的良好势头，特别是对朱一龙的表现更是赞不绝口，就连现场拍摄花絮都被大火津津乐道，有网友说：“朱一龙做单脚俯卧撑真的太苏了，肌肉线条饱满，充满力量，一双大手可以完美抓地，特别有安全感。”还有网友说：“从新边就觉得朱一龙打戏特别好看，从这个俯卧撑看来平时应该不少健身，叛逆者里也是又摔又打的。”更有网友说：“朱一龙说爽安慰群演也太暖心了一龙林楠笙真的很迷人啊！”《叛逆者》，林楠笙的表现能让朱一龙首部谍战剧能出圈吗？

    我们都知道，这些年谍战剧的影视作品拍了不少，但是让观众过目不忘的没几部，有些作品甚至成了编导们“放飞自我”的笑柄，天马行空，怎么热闹就怎么来，观众也纷纷投诉称“侮辱我们的智商！”其实听到《叛逆者》将要上线时也有不少网友有过这样的疑虑，但是《叛逆者》播出几集后，大伙不仅觉得的人物智商在线，几个主要角色无论是正派反派，都相当不简单；他们的行动，是有逻辑，而不是依靠编导的“金手指”或是“想当然”。我们也知道，谍战剧不一定要强情节、强冲突，但一定需要有强逻辑。毕竟潜伏、情报交换、策反等工作，都离不开智斗。因此，谍战剧最怕的是逻辑不在线，情节有刺眼的bug；或者为了体现我方的智慧，刻意把敌方“愚蠢化”了，一边倒的斗争没有看点，势均力敌的斗争才好看也最显激烈，也更能体现我方的胜利来之不易。看来《叛逆者》为了不让观众拧巴正是下了不少功夫。

    不得不说，《叛逆者》的演员阵容也堪称豪华，无论是朱一龙、童瑶和王志文，还是配角的王阳、朱珠、李强、姚安濂等均属实力派，虽然朱一龙是男一号，但是大伙看到王志文出现就笃定这部电视剧错不了，因为人们一致认为王志文是个对剧本对角色十分挑剔的演员，而且王志文的台词功底十分了得，这是因为人家1988年在北京电影学院毕业，他就当上了中央戏剧学院任讲师，教育学生台词，基本上，就是人家老本行，相当的专业，精英中的精英。所以当知道王志文饰演顾主任人们就期待就不仅看他怎么演，还要看听他怎么说。《叛逆者》，林楠笙的表现能让朱一龙首部谍战剧能出圈吗？

    说实话，小编期当决定追剧也是冲着王志文，因为此前有人说过，王志文一年中只拍半年的戏，后续的半年用来休息。所以不难看出，他在选择剧本上还是很讲究的，重质不重量。尽管在《叛逆者》中王志文出场有限，但是只要他一亮相，观众就会感到眼前一亮。

    当然了，在《叛逆者》这部戏中，作为男主角的朱一龙的表现也是可圈可点。他饰演的林楠笙是一个刚毕业的学生，为了报国投笔从戎，却在机缘巧合下被陈站长看中。由于林楠笙是个菜鸟，即使到了特务处里也得表现得很木讷、很拘谨。另外，他又是一个天才少年，渴望立功得到领导赏识，因此他在工作上又是非常拼。不得不说，朱一龙把这个角色塑造得很饱满。对于角色拿捏恰到好处。《叛逆者》，林楠笙的表现能让朱一龙首部谍战剧能出圈吗？

   王阳饰演的陈站长属实让人感到了惊喜。伴随着拷打声和雨声，再加上昏暗的灯光点缀，陈站长的出场环境就预示着这是一个大反派。果然，这个角色是个特务头子，不仅心狠手辣，而且极其聪明。王阳把这个角色的阴狠演绎的极其到位，无论是台词还是表情处理都拿捏的恰到好处，而且，他在和老戏骨王志文对戏时也丝毫不落下风，可以窥见演技。

    另外《叛逆者》在人物关系处理上，没有故弄玄虚，尤其在一是林楠笙和左秋明的关系，寥寥几笔，在陈默群选拔新人的过程中，这两人之间单纯、真挚的知己情就在观众心里构建出来了。虽然时间上简短，但是从一起训练、考核中互相帮扶的同甘共苦，到送笔握手的真诚祝福和敬礼目送林楠笙离开的深切不舍，情感徐徐推进感染力不断递增，左秋明在林楠笙心里的份量，已经不言自明。这为后边矛盾的爆发，林楠笙的“叛逆”，做了一个足够有力的基础。

   其次是林楠笙与陈默群的关系，也是非常简短快速地就交代明白，他为什么重用林楠笙，林楠笙又为什么会因他的“叛变”陷入崩溃与迷茫。从刚一见面开始，陈其实一直在试探林，不仅是业务能力上的试探，还有时不时的威压，林楠笙在专业上表现出色，面对威压却有着敏感真挚的青涩，是个好操控的手下，他想。在给林楠笙量衣服的时候，他那种没体验过的惊讶新奇，通过单纯的眼神和时不时的发愣表现出来，结果就是裁缝说一句他做一句，还要扭头不确定的看看陈默群，面对这么一个小伙子，陈默群忍不住笑了但是还没等完全笑出来就快速掩盖了，是个单纯的有点可爱的孩子。

    然而，陈默群忽视了最关键的一点，林楠笙有信仰，虽然朴实到有些简陋，就是“报效祖国”，还是觉得教育不能救国弃笔从戎来的，很显然没有想好嘛，还是一腔热血的小年轻而已，好好打磨就行。他轻视信仰，他不知道这是那个年代最珍贵东西，所以他必将为自己的高傲付出代价。《叛逆者》，林楠笙的表现能让朱一龙首部谍战剧能出圈吗？

    小编以为，《叛逆者》好就好在，演员的表演也十分贴合，对角色的把握准确，目前出场的每个主要人物都非常鲜明，靠谱团队的通力配合是成就好作品的保障，这方面《叛逆者》无疑是做到了。兴许，现在就说《叛逆者》一定成为年度“爆款”还为时太早，但是最起码《叛逆者》现在已经有“爆款”的样子了！（随意）"""
    data = get_a_list(text)
    get_word_cloud(data)



















