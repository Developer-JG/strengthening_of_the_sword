from random import randint
from random import choice

print("\nstrengthening of the sword game project\n\n\n")

# 플래이어 클래스
class player:
    def __init__(self, sword, money, prevention_item, inventory):
        self.sword = sword
        self.money = money
        self.prevention_item = prevention_item
        self.inventory = {"sword": [], "item": []}

# 일반 아이템 클래스
class common_item:
    def __init__(self, name):
        self.name = name

# 판매 아이템 클래스
class shop_item:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

# 아이템
# 일반 아이템
item_00 = common_item("깨짐 방지권")
item_01 = common_item("국적불분명 철조각")
item_02 = common_item("타우의 뼈 부스러기")
item_03 = common_item("빛 바랜 형광물질")
item_04 = common_item("스워스산 철조각")
item_05 = common_item("불꽃마검 손잡이")
item_06 = common_item("사악한 영혼")
item_07 = common_item("도끼 가루")
item_08 = common_item("투명 물질")
# 판매 아이템
item_11 = shop_item("깨짐 방지권 X 1", 1000000)
item_12 = shop_item("깨짐 방지권 X 3", 2500000)
item_13 = shop_item("+9강 워프권", 1000000)
item_14 = shop_item("+13강 워프권", 7000000)
item_15 = shop_item("+14강 워프권", 10000000)
item_16 = shop_item("+15강 워프권", 15000000)

# 검 클래스
class sword:
    def __init__(self, name, reinforcement_cost, selling_price, success_rate, prevention, required_item, required_item_count, drop_item, drop_item_count):
        self.name = name
        self.reinforcement_cost = reinforcement_cost
        self.selling_price = selling_price
        self.success_rate = success_rate
        self.prevention = prevention
        self.required_item = required_item
        self.required_item_count = required_item_count
        self.drop_item = drop_item
        self.drop_item_count = drop_item_count

# 검 종류
# 검 이름, 강화비용, 판매가격, 성공률, 방지권, 필요아이템, 드랍아이템
sword_0 = sword("+0 낡은 단검", 300, 0, 100, 0, "", 0, "", 0)
sword_1 = sword("+1 쓸만환 단검", 300, 150, 100, 0, "", 0, "", 0)
sword_2 = sword("+2 견고한 단검", 500, 400, 100, 0, "", 0, "", 0)
sword_3 = sword("+3 바이킹 소드", 500, 600, 95, 0, "", 0, "", 0)
sword_4 = sword("+4 불타는 검", 1000, 800, 95, 0, "", 0, "", 0)
sword_5 = sword("+5 냉기의 소드", 1500, 1600, 90, 0, "", 0, "", 0)
# 방지권
sword_6 = sword("+6 양날 검", 2000, 3500, 90, 1, "", 0, item_01, 2)
sword_7 = sword("+7 심판자의 대검", 2000, 6100, 90, 1, "", 0, item_01, 3)
sword_8 = sword("+8 마력의 검", 3000, 10000, 85, 1, "", 0, item_01, 5)
sword_9 = sword("+9 타우 스워드", 5000, 20000, 80, 1, "", 0, item_02, 1)
sword_10 = sword("+10 형광 검", 10900, 35100, 80, 1, "", 0, item_03, 2)
sword_11 = sword("+11 피묻은 검", 20000, 160000, 75, 1, "", 0, item_04, 2)
sword_12 = sword("+12 화염의 쌍검", 35000, 350000, 70, 1, "", 0, item_04, 4)
sword_13 = sword("+13 불꽃 마검", 5000, 20000, 80, 2, "", 0, item_05, 1)
sword_14 = sword("+14 마검 아포피스", 100000, 3000000, 65, 3, "", 0, item_06, 3)
sword_15 = sword("+15 데몬 배틀 엑스", 180000, 7500000, 60, 4, "", 0, item_07, 3)
sword_16 = sword("+16 투명 검", 300000, 14200000, 60, 7, "", 0, item_08, 2)
sword_17 = sword("+17 날렵한 용검", 300000, 30000000, 55, 9, "", 0, "", 0)
sword_18 = sword("+18 샤이니 소드", 500000, 30000000, 50, 10, "", 0, "", 0)
# 보관
sword_19 = sword("+19 왕푸야샤", 800000, 47500000, 50, 12, "", 0, "", 0)
sword_20 = sword("+20 다색검", 1500000, 68300000, 45, 15, "", 0, "", 0)
sword_21 = sword("+21 템페스트 골드", 0, 101000000, 40, 17, sword_19, 1, "", 0)
sword_22 = sword("+22 샤프 워커", 0, 160000000, 40, 20, sword_21, 2, "", 0)
sword_23 = sword("+23 삐에로의 쌍검", 0, 230000000, 40, 22, item_06, 12, "", 0)
sword_24 = sword("+24 도룡도", 0, 300000000, 40, 23, sword_22, 1, "", 0)
sword_25 = sword("+25 안 강해보이는 검", 0, 400000000, 35, 23, item_07, 15, "", 0)
sword_26 = sword("+26 메두사", 5000000, 1800000000, 50, 0, "", 0, "", 0)
sword_27 = sword("+27 오딧세이 소드", 0, 2500000000, 40, 0, item_08, 2, "", 0)
sword_28 = sword("+28 모자이칼", 0, 0, 15, 0, "", 0, "", 0)
sword_29 = sword("+29 화염에 달군 검", "Unkown", "Unkown", "Unkown", 0, "", 0, "", 0)

sword_list_01 = [sword_0, sword_1, sword_2, sword_3, sword_4, sword_5]
sword_list_02 = [sword_6, sword_7, sword_8, sword_9, sword_10, sword_11, \
                sword_12, sword_13, sword_14, sword_15, sword_16, sword_17, \
                sword_18]
sword_list_03 = [sword_19, sword_20, sword_21, sword_22, sword_23, sword_24, \
                sword_25, sword_26, sword_27, sword_28, sword_29]
sword_list_11 = [sword_0, sword_1, sword_2, sword_3, sword_4, sword_5, \
                 sword_6, sword_7, sword_8, sword_9, sword_10, sword_11, \
                sword_12, sword_13, sword_14, sword_15, sword_16, sword_17, \
                sword_18]

# 강화하기
def reinforcement(player_1):
    if player_1.sword.reinforcement_cost <= player_1.money:
        player_1.money -= player_1.sword.reinforcement_cost
        percentage = choice("y" * player_1.sword.success_rate + "n" * (100 - player_1.sword.success_rate))
        if percentage == "y":
            print("성공\n")
        elif percentage == "n":
            print("실패\n")
    else:
        print("돈이 부족합니다.")

# 상점
def shop():
    pass

# 인벤토리
def inventory():
    pass

# 보관하기
def keep():
    pass

# 메인
def main():
    print("(이 게임은 9칸의 로그 화면을 요구합니다.)\n")
    input("게임을 시작하려면 엔터")

    print("\n" * 38)

    player_1 = player(sword_0, 1000000, 0, [])

    while True:
        if player_1.sword == sword_0:
            print("강화하기 : q / 상점 : w / 인벤토리 : e\n\n")
        elif player_1.sword == sword_28:
            print("강화하기 : q\n\n")
        elif player_1.sword in sword_list_11:
            print("강화하기 : q / 판매하기 : w\n\n")
        elif player_1.sword in sword_list_03:
            print("강화하기 : q / 판매하기 : w / 보관하기 : e\n\n")

        if player_1.sword.reinforcement_cost == 0 and player_1.sword != swrod_28:
            print(f"{player_1.sword.name}\n강화 성공률 : {player_1.sword.success_rate}% / 깅화재료 : {player_1.sword.required_item} X {player_1.sword.required_item_count} \
                  판매가격 : {player_1.sword.selling_price}\n방지권 : {player_1.prevention_item} 돈 : {player_1.money}")
        else:
            print(f"{player_1.sword.name}\n강화 성공률 : {player_1.sword.success_rate}% / 깅화비용 : {player_1.sword.reinforcement_cost} 판매가격 : {player_1.sword.selling_price} \
                \n방지권 : {player_1.prevention_item} 돈 : {player_1.money}")

        answer = input("= ")
        if answer == "q":
            reinforcement(player_1)
        elif answer == "w":
            if player_1.sword == "sword_0":
                shop()
            elif player_1.sword != "sword_28":
                shop()
            else:
                print("\n다시 입력해 주십시오.\n")
        elif answer == "e":
            if player_1.sword == "sword_0":
                inventory()
            elif player_1.sword in sword_list_03:
                keep()
            else:
                print("\n다시 입력해 주십시오.\n")
        else:
            print("\n다시 입력해 주십시오.\n")

# print("강화가 실패하여 검이 파괴되었습니다.")


if __name__ == "__main__":
    main()