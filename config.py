from enum import Enum

token = '563920986:AAEq9PZMvR0FFsTLnpUX3UfoDxO4sr_B2P4'
quest_db = '/Users/borispetrusev/PycharmProjects/telegrambot/venv/db_quest'
user_state_db = '/Users/borispetrusev/PycharmProjects/telegrambot/venv/db_user_state.vdb'

class States(Enum):

    S_START = "0"
    S_LANG_SELECT = "0_LANG"
    S_BRANCH_0_1_ENG = "branch_0_1_eng"
    S_BRANCH_0_1_RU = "branch_0_1_ru"
    S_BRANCH_END_1_RU = "branch_1_1_ru"
    S_BRANCH_END_2_RU = "branch_1_2_ru"
    S_BRANCH_END_3_RU = "branch_1_3_ru"
    S_BRANCH_END_4_RU = "branch_1_4_ru"
    S_BRANCH_END_5_RU = "branch_1_5_ru"
    S_BRANCH_END_6_RU = "branch_1_6_ru"
    S_BRANCH_END_7_RU = "branch_1_7_ru"
    S_BRANCH_END_8_RU = "branch_1_8_ru"
    S_BRANCH_END_9_RU = "branch_1_9_ru"
    S_BRANCH_END_10_RU = "branch_1_10_ru"
    S_BRANCH_END_11_RU = "branch_1_11_ru"



