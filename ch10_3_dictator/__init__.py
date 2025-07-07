from otree.api import *
import random

doc = """ """


class C(BaseConstants):
    NAME_IN_URL = "ch10_3_dictator"
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1
    ENDOWMENT = 100
    INSTRUCTIONS_TEMPLATE = "ch10_3_dictator/instructions.html"
    ADD_TIME = 180

    CHOICE_LIST_SENTE = [
        [0, "あなた0ポイント、相手100ポイント"],
        [10, "あなた10ポイント、相手90ポイント"],
        [20, "あなた20ポイント、相手80ポイント"],
        [30, "あなた30ポイント、相手70ポイント"],
        [40, "あなた40ポイント、相手60ポイント"],
        [50, "あなた50ポイント、相手50ポイント"],
        [60, "あなた60ポイント、相手40ポイント"],
        [70, "あなた70ポイント、相手30ポイント"],
        [80, "あなた80ポイント、相手20ポイント"],
        [90, "あなた90ポイント、相手10ポイント"],
        [100, "あなた100ポイント、相手0ポイント"],
    ]


class Subsession(BaseSubsession):
    num_participants_p1 = models.IntegerField(initial=0)
    num_participants_p2 = models.IntegerField(initial=0)
    num_100 = models.IntegerField(initial=0)
    num_90 = models.IntegerField(initial=0)
    num_80 = models.IntegerField(initial=0)
    num_70 = models.IntegerField(initial=0)
    num_60 = models.IntegerField(initial=0)
    num_50 = models.IntegerField(initial=0)
    num_40 = models.IntegerField(initial=0)
    num_30 = models.IntegerField(initial=0)
    num_20 = models.IntegerField(initial=0)
    num_10 = models.IntegerField(initial=0)
    num_0 = models.IntegerField(initial=0)
    num_accept = models.IntegerField(initial=0)
    num_reject = models.IntegerField(initial=0)

    num_participants = models.IntegerField(initial=0)

    err_message = models.StringField()
    err_message_pair = models.StringField()


class Group(BaseGroup):
    p1_amount = models.IntegerField()
    p2_amount = models.IntegerField()

    p1_decision = models.StringField(
        choices=C.CHOICE_LIST_SENTE, widget=widgets.RadioSelect, label=""
    )
    p1_decision_why = models.LongStringField(label="なぜその選択をしましたか？")

    flg_non_input_p1 = models.IntegerField(initial=0)


class Player(BasePlayer):
    pass


# FUNCTIONS
def set_P1(player: Player):
    sub = player.subsession
    group = player.group

    sub.num_participants += 1
    if group.p1_decision != "":
        sub.num_participants_p1 += 1
        print("++++++++++++++++", group.p1_decision)
        s = group.p1_decision
        if s == "100":
            sub.num_100 += 1
        elif s == "90":
            sub.num_90 += 1
        elif s == "80":
            sub.num_80 += 1
        elif s == "70":
            sub.num_70 += 1
        elif s == "60":
            sub.num_60 += 1
        elif s == "50":
            sub.num_50 += 1
        elif s == "40":
            sub.num_40 += 1
        elif s == "30":
            sub.num_30 += 1
        elif s == "20":
            sub.num_20 += 1
        elif s == "10":
            sub.num_10 += 1
        elif s == "0":
            sub.num_0 += 1
        else:
            sub.err_message = "エラーあり"
    else:
        group.flg_non_input_p1 = 1
        tmp = random.randint(0, 10)
        group.p1_decision = str(C.CHOICE_LIST_SENTE[tmp][0])
    # 先手の配分計算
    # group.p1_amount = C.ENDOWMENT - int(group.p1_decision)
    # group.p1_amount = C.ENDOWMENT - int(group.p1_decision)
    group.p1_amount = int(group.p1_decision)
    group.p2_amount = C.ENDOWMENT - int(group.p1_decision)


def set_P1s(subsession: Subsession):
    for p in subsession.get_players():
        set_P1(p)


def set_payoffs(group: Group):
    p1 = group.get_player_by_id(1)
    p2 = group.get_player_by_id(2)

    # p1.payoff = C.ENDOWMENT - int(group.p1_decision)
    # p2.payoff = int(group.p1_decision)
    p1.payoff = int(group.p1_decision)
    p2.payoff = C.ENDOWMENT - int(group.p1_decision)
    graph(subsession=group.subsession)


def graph(subsession: Subsession):
    sub = subsession
    session = sub.session
    graph_list = []

    ch10_3_result = []

    # 割合に計算(accept)
    if sub.num_0 > 0:
        tmp = round((sub.num_0 / sub.num_participants) * 100, 2)
        graph_list.append(tmp)
    else:
        graph_list.append(0)
    if sub.num_10 > 0:
        tmp = round((sub.num_10 / sub.num_participants) * 100, 2)
        graph_list.append(tmp)
    else:
        graph_list.append(0)
    if sub.num_20 > 0:
        tmp = round((sub.num_20 / sub.num_participants) * 100, 2)
        graph_list.append(tmp)
    else:
        graph_list.append(0)
    if sub.num_30 > 0:
        tmp = round((sub.num_30 / sub.num_participants) * 100, 2)
        graph_list.append(tmp)
    else:
        graph_list.append(0)
    if sub.num_40 > 0:
        tmp = round((sub.num_40 / sub.num_participants) * 100, 2)
        graph_list.append(tmp)
    else:
        graph_list.append(0)
    if sub.num_50 > 0:
        tmp = round((sub.num_50 / sub.num_participants) * 100, 2)
        graph_list.append(tmp)
    else:
        graph_list.append(0)
    if sub.num_60 > 0:
        tmp = round((sub.num_60 / sub.num_participants) * 100, 2)
        graph_list.append(tmp)
    else:
        graph_list.append(0)
    if sub.num_70 > 0:
        tmp = round((sub.num_70 / sub.num_participants) * 100, 2)
        graph_list.append(tmp)
    else:
        graph_list.append(0)
    if sub.num_80 > 0:
        tmp = round((sub.num_80 / sub.num_participants) * 100, 2)
        graph_list.append(tmp)
    else:
        graph_list.append(0)
    if sub.num_90 > 0:
        tmp = round((sub.num_90 / sub.num_participants) * 100, 2)
        graph_list.append(tmp)
    else:
        graph_list.append(0)
    if sub.num_100 > 0:
        tmp = round((sub.num_100 / sub.num_participants) * 100, 2)
        graph_list.append(tmp)
    else:
        graph_list.append(0)

    for player in subsession.get_players():
        group = player.group
        participant = player.participant
        participant.vars["ch10_3_result"] = (
            "++++++++++++++++++++++++++++++++++++++++++++++++++<br>"
            "独裁者ゲーム：あなたの結果："
            "プレイヤー1（先手）は、プレイヤー1に"
            + str(group.p1_amount)
            + "ポイント、プレイヤー2に"
            + str(group.p2_amount)
            + "という提案をしました。<br>"
            "プレイヤー2（後手）は、プレイヤー1の提案をそのまま受け入れます。<br>"
            "++++++++++++++++++++++++++++++++++++++++++++++++++"
        )

    ch10_3_result.append(participant.vars["ch10_3_result"])

    #  最終結果用
    if "graph_data" not in session.vars:
        session.graph_data = {}
    session.graph_data["ch10_3"] = {
        "num_participants": sub.num_participants,
        "graph_list": graph_list,
        "ch10_3_result": ch10_3_result,
    }


# PAGES-----
class Introduction(Page):
    timeout_seconds = 60


class Send(Page):
    # timeout_seconds = 60+C.ADD_TIME
    timeout_seconds = C.ADD_TIME
    form_model = "group"
    form_fields = ["p1_decision", "p1_decision_why"]

    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == 1


class WaitForP1(WaitPage):
    wait_for_all_groups = True
    after_all_players_arrive = set_P1s


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs


class Results(Page):
    @staticmethod
    def js_vars(player: Player):
        print("js_vars")
        return player.session.graph_data


page_sequence = [Introduction, Send, WaitForP1, ResultsWaitPage, Results]
