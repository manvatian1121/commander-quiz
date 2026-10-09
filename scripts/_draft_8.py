# -*- coding: utf-8 -*-
"""descriptions_8.json 的草稿。

牌名一律用 {English Name} 占位，由 build_descriptions_8.py 机械替换成
「中文名（English Name）」——中文名只从 card_zh.json / commander_zh.json 取，
不凭记忆写译名。占位符若不在该主将自己的清单里，构建时会直接报错。
"""

CONTENT = {

    # ---------------- batch 1 ----------------
    "Zur the Enchanter": {
        "tagline": "主将一攻击，就白拿一个结界",
        "intro": "{Zur the Enchanter}是白蓝黑三色的四费法师，自己会飞。它每次攻击都会免费从牌库里翻出一张费用不大的结界，直接放进场，所以你越早让它打中一次，好处来得越快。喜欢提前布置、一点点把局势锁住的人会喜欢它。",
        "build": "牌表以结界为主：{Ghostly Prison}和{Propaganda}让对手攻击你时先多付法术力，{Grasp of Fate}一次封住每位对手的一个非地永久物。给主将贴上{All That Glitters}，它会变成很大的攻击者，而且每次攻击都多带一张结界进场。新人注意：主将怕被反击，前期别让它单独冲上去。",
    },
    "Aesi, Tyrant of Gyre Strait": {
        "tagline": "每落一块地，就多抽一张牌",
        "intro": "{Aesi, Tyrant of Gyre Strait}是蓝绿两色的六费巨蛇。它让你每回合多放一块地，而且只要有一块地进场，你就抽一张牌。这套牌靠的是地越铺越多、手牌一直有补充，不靠打人。喜欢慢慢变大的玩家会喜欢它。",
        "build": "{Azusa, Lost but Seeking}让你一回合多放两块地，{Explore}和{Growth Spiral}也帮你多放地并顺手抽牌。地铺开之后，{Avenger of Zendikar}会带出一群生物替你收尾。新人注意：别怕手上地多，但也别把牌用光。",
    },
    "Urza, Chief Artificer": {
        "tagline": "神器越多，场上的机器越大",
        "intro": "{Urza, Chief Artificer}是白蓝黑三色的六费神器师。你场上的神器生物都有威慑，对手要用两只以上才挡得住；每个回合结束，它还会免费给你一个跟自家神器数量一样大的机器生物。喜欢把一桌小神器滚大的人会喜欢它。",
        "build": "牌表里有很多神器地，像{Seat of the Synod}和{Ancient Den}，它们既产法术力，又让每回合白来的那个机器更大。{Etherium Sculptor}让神器咒语更便宜，{Sai, Master Thopterist}在你放神器时不断给你小飞机。新人注意：主将费用不低，前期先铺便宜神器。",
    },
    "Alela, Artful Provocateur": {
        "tagline": "放神器或结界，就多一只小飞仙",
        "intro": "{Alela, Artful Provocateur}是白蓝黑三色的四费仙灵，自己会飞，还带死触和系命。你每放一张神器或结界，它就免费给你一只会飞的小仙灵，自家会飞的生物也都大一点。喜欢一边铺场一边回血、用小飞兵淹过去的人会喜欢它。",
        "build": "{Bitterblossom}每回合自动给你一只小仙灵，{Favorable Winds}和{Intangible Virtue}让这些小家伙一起变大，{Obyra, Dreaming Duelist}在你每多一只仙灵进场时就让对手掉血。新人注意：仙灵很小，遇到清场会一次全没，别把希望全押在它们身上。",
    },
    "Morophon, the Boundless": {
        "tagline": "选一个种族，全族都变便宜",
        "intro": "{Morophon, the Boundless}是五色的七费变形兽。它进场时你要选一个生物类别，比如龙或者鬼怪；之后你放的这类生物咒语会便宜一大截，自家同类生物也都会大一点。适合一开始就想好「我要组一套全是某某族」的玩家。",
        "build": "{Urza's Incubator}和{Herald's Horn}让选定的那类咒语更便宜，{Realmwalker}让你能一直从牌库顶挑同类生物来放，{Maskwood Nexus}则让自家所有生物都算作你选的类别。新人注意：先想好种族，再照着它配牌。",
    },
    "Zada, Hedron Grinder": {
        "tagline": "一张小咒语，全队一起受益",
        "intro": "{Zada, Hedron Grinder}是红色的四费鬼怪。它的本事很特别：只要你放的瞬间或法术只指它自己，这个咒语就会为场上每只别的生物各复制一份。所以一张「抽一张牌」的小咒语会变成全队一起抽。喜欢用便宜小牌打配合的人会喜欢它。",
        "build": "{Expedite}和{Crimson Wisps}让全队获得敏捷并抽一张牌，{Fists of Flame}让每只生物都加上践踏和攻击力，{Dragon Fodder}负责铺开小鬼怪给你复制。{Storm-Kiln Artist}在你放或复制咒语时不断给你宝物。新人注意：咒语只能指主将一个人，否则复制不了。",
    },
    "Magus Lucea Kane": {
        "tagline": "花多少费用，都会再来一份",
        "intro": "{Magus Lucea Kane}是蓝绿红三色的四费法师。它每回合战斗前给一只生物加一层指示物，还能产出两点无色法术力；关键是你接下来放的那张费用里带变量的咒语会直接再来一份。喜欢一口气砸出一只超大生物的人会喜欢它。",
        "build": "核心是一堆费用带变量的生物，比如{Hydroid Krasis}、{Aberrant}和{Tervigon}：你把法术力全花在上面，它们就带着成堆的指示物进场，而主将会把这一下原样再复制一次，等于白来一只。{Unbound Flourishing}让变量翻倍。新人注意：想复制就得留法术力给主将。",
    },

    # ---------------- batch 2 ----------------
    "Satoru Umezawa": {
        "tagline": "小生物打过去，换大生物偷袭",
        "intro": "{Satoru Umezawa}是蓝黑两色的三费忍者。它让手上每一张生物牌都能用「忍术」便宜地换上场：先派一只没人挡得住的小生物攻击，再把手里的大生物换进去，直接横着进场并参加这次攻击。喜欢偷袭、用小生物骗过对手的人会喜欢它。",
        "build": "{Slither Blade}和{Mist-Cloaked Herald}这类不能被阻挡的小生物是起手最想要的，有它们在，你每回合都能把手里的大生物换上场；{Silver-Fur Master}让这些交换更便宜，每次换人还能从牌库顶挑一张进手。新人注意：忍术只能在攻击者没被挡住之后用。",
    },
    "Inalla, Archmage Ritualist": {
        "tagline": "每只法师，都能多来一只",
        "intro": "{Inalla, Archmage Ritualist}是蓝黑红三色的五费人类法师。就算她还没上场，你放法师生物时也能付一点法术力，让那只法师多来一只复制品。喜欢反复利用生物进场效果、把好处滚大的人会喜欢她。",
        "build": "关键是挑进场就有好处的法师：{Archaeomancer}能把坟场里的瞬间或法术拿回手上，{Bloodline Necromancer}能把坟场里的法师拉回场上，复制出来的那只还会再触发一次。{Naban, Dean of Iteration}让这些效果再多来一次。新人注意：复制来的那只回合结束就被放逐。",
    },
    "Omnath, Locus of All": {
        "tagline": "五色大手牌，法术力不浪费",
        "intro": "{Omnath, Locus of All}是五色的五费元素。你每个回合都会先看一眼牌库顶、把它拿到手里，如果那张牌的颜色够杂，还会顺带给你三点法术力；没花完的法术力也不会白消失，会变成黑色法术力留着。喜欢手里牌多的玩家会喜欢它。",
        "build": "靠大量不同颜色的地撑起五色，{Faeburrow Elder}也能按你场上颜色的数量产法术力。赢法是把省下的法术力砸在贵的多色牌上：{Ruinous Ultimatum}一次清掉对手全场的非地永久物，{Villainous Wealth}直接从对手牌库顶挖走一堆牌免费使用。新人注意：凑齐五色是前提。",
    },
    "Kykar, Wind's Fury": {
        "tagline": "放非生物咒语，就多一只小精怪",
        "intro": "{Kykar, Wind's Fury}是蓝红白三色的四费鸟法师，自己会飞。你每放一个不是生物的咒语，它就给你一只会飞的小精怪；这些小精怪还能被牺牲掉换成红色法术力，让你继续放咒语。喜欢法术不断、场面越铺越满的玩家会喜欢它。",
        "build": "牌表里塞满便宜的瞬间和法术，{Brainstorm}和{Opt}这种一张就能换一只小精怪；{Impact Tremors}让每只新来的生物都让对手掉一点血，{Whirlwind of Thought}则在你每放一个非生物咒语时补一张牌。新人注意：精怪既是兵也是法术力，牺牲前先想清楚。",
    },
    "The Scarab God": {
        "tagline": "把坟场里的生物，变成自己的僵尸",
        "intro": "{The Scarab God}是蓝黑两色的五费神。它能把双方坟场里的生物挖出来，变成一只黑色僵尸替你作战；你场上的僵尸越多，它每个回合开始时就让每位对手掉越多血。而且它就算被打死，也会自己回到你手上。喜欢把坟场当资源用的人会喜欢它。",
        "build": "{Rooftop Storm}让你放僵尸生物几乎不用花法术力，{Death Baron}和{Diregraf Captain}给全队僵尸加强，{Gray Merchant of Asphodel}进场时按你黑色法术力符号的数量让每位对手掉血。新人注意：主将费用不低，前期先靠便宜的僵尸站住场面。",
    },
    "Winota, Joiner of Forces": {
        "tagline": "小飞机打过去，白拉一个人类",
        "intro": "{Winota, Joiner of Forces}是红白两色的四费人类战士。每当一只不是人类的生物攻击，它就翻牌库顶六张，翻到人类就直接放进场一起打，而且这回合不会被消灭。喜欢「一攻击就白来人」的玩家会喜欢它。",
        "build": "{Ornithopter}和{Gingerbrute}都是很便宜的小攻击者，专门用来触发主将；翻出来的人类里，{Blade Historian}让所有攻击生物打出两倍伤害，{Angrath's Marauders}让伤害整体翻倍。新人注意：触发只认「不是人类的生物」在攻击，别只放人类。",
    },
    "Prosper, Tome-Bound": {
        "tagline": "牌库顶的那张，早晚都是我的",
        "intro": "{Prosper, Tome-Bound}是黑红两色的四费提夫林，自带死触。它每回合结束都会把牌库顶一张牌放逐，而你可以在一轮之内把它当手牌用掉；只要你从放逐区用了牌，它就还你一枚宝物。喜欢「资源总比别人多一份」的玩家会喜欢它。",
        "build": "{Xorn}让你每次做宝物都多做一枚，{Wild-Magic Sorcerer}让你从放逐区放的第一张咒语顺带再白放一张。{Reckless Fireweaver}在宝物进场时就让对手掉血，{Mayhem Devil}则在你牺牲宝物换法术力时补上伤害。新人注意：放逐出来的那张只能用到下个回合结束，别攒着。",
    },

    # ---------------- batch 3 ----------------
    "Sythis, Harvest's Hand": {
        "tagline": "放结界就回血抽牌，越放越多",
        "intro": "{Sythis, Harvest's Hand}是白绿两色的二费结界生物，规则很短：你每放一个结界咒语，就回一点血并抽一张牌。它两费就能上场，所以这套牌从第一两个回合起就不停放结界、不停补牌。喜欢规则简单的玩家会喜欢它。",
        "build": "牌表里几乎全是结界：{Wild Growth}和{Utopia Sprawl}贴在自家地上，让每块地多产法术力；{Sanctum Weaver}按你场上结界的数量产法术力。{Sigil of the Empty Throne}则不断为你带来会飞的天使。新人注意：主将很小，被针对时很难受。",
    },
    "Marchesa, the Black Rose": {
        "tagline": "带指示物的生物，死了还能回来",
        "intro": "{Marchesa, the Black Rose}是蓝黑红三色的四费人类法师。只要一只带指示物的生物死掉，它下个回合结束时就会自己爬回场上。所以你不用怕清场，还能主动牺牲自家生物换好处。喜欢反复利用同一批生物的人会喜欢她。",
        "build": "{Unspeakable Symbol}让你花血给生物加指示物，{Carrion Feeder}和{Ashnod's Altar}负责把生物牺牲掉换好处。{Flayer of the Hatebound}在生物从坟场回场时会打对手一大下。新人注意：先给生物加上指示物再牺牲，顺序反了就回不来了。",
    },
    "Tiamat": {
        "tagline": "主将一进场，手上多五条龙",
        "intro": "{Tiamat}是五色的七费龙神，自己会飞。它进场时会从牌库里直接找出五条名字各不相同的龙放进手牌，等于一次把弹药全拿到手，之后你只要一张一张把它们放出来就行。喜欢龙、喜欢大生物压场的玩家几乎都会选它。",
        "build": "{Dragonspeaker Shaman}让龙咒语更便宜，{Dragon Tempest}在每条龙进场时按你场上龙的数量打一下任意目标，{Lathliss, Dragon Queen}和{Miirym, Sentinel Wyrm}则会不断给你更多龙。新人注意：主将七费不便宜，前期要把费用攒够。",
    },
    "Najeela, the Blade-Blossom": {
        "tagline": "战士一攻击，就多一个战士",
        "intro": "{Najeela, the Blade-Blossom}是五色的三费战士。每当一个战士攻击，就免费再多一个横着进场、也在攻击的战士，场面像雪球一样越打越多。它还能付五色各一点，让全体攻击者站起来再打一次。喜欢人海战术的玩家会喜欢它。",
        "build": "{Birds of Paradise}和{Wooded Foothills}这类能产任意颜色、能找地的牌，负责把五色凑齐，这是最重要的功课。{Druids' Repository}在你每次攻击时攒指示物再换成法术力，好让你反复启动主将的能力。新人注意：这套牌最怕卡色，地要配得讲究。",
    },
    "Shelob, Child of Ungoliant": {
        "tagline": "被蜘蛛咬死的生物，变成食物",
        "intro": "{Shelob, Child of Ungoliant}是黑绿两色的六费蜘蛛恶魔，自家其他蜘蛛和它一样有死触；被它们咬过又死掉的生物会变成食物留给你，食物能换来三点生命。这套牌靠一群蜘蛛守住场面慢慢赚。喜欢稳守的玩家会喜欢它。",
        "build": "{Twin-Silk Spider}和{Arasta of the Endless Web}都会带来新蜘蛛，{Arachnogenesis}能在对手大举进攻时变出一群蜘蛛挡下来。{Twitching Doll}能产任意颜色的法术力，还能牺牲自己换一只蜘蛛。新人注意：靠蜘蛛咬伤对手生物赚食物，主动去打不是重点。",
    },
    "Rocco, Street Chef": {
        "tagline": "有人从放逐区出牌，我就加菜",
        "intro": "{Rocco, Street Chef}是红绿白三色的三费妖精德鲁伊，也是位「请客」型主将：每回合结束，每位玩家都从牌库顶翻一张，谁都能用；只要有人从放逐区用牌或放地，你就给自家生物加指示物、还多一块食物。喜欢热闹的玩家会喜欢它。",
        "build": "{Night of the Sweets' Revenge}让食物能当法术力用，{Jaheira, Friend of the Forest}让自家衍生物都能产法术力，正好把食物换成放出大生物的钱。{Academy Manufactor}让你每次做食物时顺便多出别的宝物。新人注意：这套牌会给对手送资源，你要拿到更多。",
    },
    "Liesa, Shroud of Dusk": {
        "tagline": "谁放咒语谁掉血，我负责回血",
        "intro": "{Liesa, Shroud of Dusk}是黑白两色的五费天使，会飞又有系命。任何玩家每放一个咒语都要掉两点血，连你自己也不例外；就算她被打死，你也能用付生命的方式把她再召唤回来。喜欢让对手处处别扭的玩家会喜欢她。",
        "build": "{Kambal, Consul of Allocation}在对手放非生物咒语时让他掉血、你回血，{Soul Warden}这类牌负责一点点攒生命。{Vito, Thorn of the Dusk Rose}把「你回血」直接变成「对手掉血」，是这套牌真正的赢法。新人注意：你自己放咒语也要掉两点血，算血时别忘了。",
    },

    # ---------------- batch 4 ----------------
    "Ramos, Dragon Engine": {
        "tagline": "多色咒语攒指示物，攒够爆法术力",
        "intro": "{Ramos, Dragon Engine}是五色的六费神器龙，自己会飞。你每放一个咒语，它就按那个咒语的颜色数攒指示物；攒够五个，你可以把它们全部换成十点五色法术力，一口气放一张很大的牌。喜欢攒一波再爆发的玩家会喜欢它。",
        "build": "牌表里全是颜色够杂的牌：{Conflux}一次从牌库找出五种颜色各一张，{Abzan Charm}这种三色牌一次就能让主将攒三层。攒出的十点法术力，正好够放{Progenitus}或启动{Door to Nothingness}。新人注意：主将被打死，攒的指示物就全没了。",
    },
    "Sefris of the Hidden Ways": {
        "tagline": "一边填坟场，一边闯地城",
        "intro": "{Sefris of the Hidden Ways}是白蓝黑三色的三费人类法师。只要你往自家坟场放进生物牌，她就带你进地城探险；地城走到头时，你就能把坟场里的生物直接拉回场上。喜欢一边送牌进坟场、一边慢慢经营的人会喜欢她。",
        "build": "{Triumphant Adventurer}和{White Plume Adventurer}都能自己带你进地城，{Radiant Solar}则在自家生物进场时帮你推进，地城会走得快很多。{Sun Titan}能把费用小的永久物从坟场反复拿回来。新人注意：每回合只会因为坟场进生物推进一次。",
    },
    "Varina, Lich Queen": {
        "tagline": "带僵尸打人，一边抽牌一边丢牌",
        "intro": "{Varina, Lich Queen}是白蓝黑三色的四费僵尸法师。你带着僵尸攻击时，几只僵尸就抽几张牌，然后丢掉同样数量的牌，同时回等量的血；丢进坟场的牌还能换成新的僵尸。喜欢坟场越堆越厚、资源越滚越多的人会喜欢她。",
        "build": "{Rooftop Storm}让你放僵尸几乎不用花法术力，{Corpse Knight}在你每只生物进场时就打对手一点血，{Wayward Servant}则在僵尸进场时让对手掉血。{Gravecrawler}只要场上有僵尸就能从坟场反复出来。新人注意：攻击时是先抽牌再丢牌，先想好丢什么。",
    },
    "Judith, Carnage Connoisseur": {
        "tagline": "小伤害配上死触，清掉对手全场",
        "intro": "{Judith, Carnage Connoisseur}是黑红两色的五费祭师。你每放一个瞬间或法术都能二选一：让它获得死触和系命，或免费多一只小恶魔。配上打一点伤害的小法术就能清掉对手全场生物；喜欢用小法术搞大事的人会喜欢她。",
        "build": "{Tectonic Hazard}和{End the Festivities}都是打一点伤害的小法术，配上死触就变成对全场的清扫。{Guttersnipe}在你每放一个瞬间或法术时打对手两点血，配合清场很容易把人磨垮。新人注意：{Blasphemous Act}会伤害场上所有生物，用之前先看看自己这边。",
    },
    "Stella Lee, Wild Card": {
        "tagline": "一回合第二个咒语，白拿一张牌",
        "intro": "{Stella Lee, Wild Card}是蓝红两色的三费人类浪客。你每回合放的第二个咒语会额外从牌库顶放逐一张牌给你用；如果你一回合放了三个以上咒语，还能横置她，把一个瞬间或法术再复制一份。喜欢连放小咒语的人会喜欢她。",
        "build": "牌表的核心是一费两费的小抽牌和调牌：{Opt}、{Preordain}和{Serum Visions}都能帮你安排牌库顶，顺便凑出「第二个咒语」。{Refocus}和{Cerulean Wisps}既便宜又能顺手抽一张，最容易凑到三个咒语好启动主将。新人注意：复制能力要这个回合已经放过三个咒语才能用。",
    },
    "Sheoldred, the Apocalypse": {
        "tagline": "你抽牌我回血，对手抽牌掉血",
        "intro": "{Sheoldred, the Apocalypse}是黑色的四费非瑞人。你每抽一张牌就回两点血，而对手每抽一张牌就掉两点血。她既是你的回血机器，也是逼着别人掉血的压力源；配上让全场抽牌的牌，对手很快撑不住。这张主将本身也不便宜。",
        "build": "{Howling Mine}让对手不停抽牌，他们每抽一张就掉两点血，{Underworld Dreams}还会补上伤害；{Peer into the Abyss}让人一次抽掉半个牌库。{Phyrexian Arena}负责你自己的抽牌。新人注意：这套牌会让对手有点难受，别在朋友局头一次就掏出来。",
    },
}
