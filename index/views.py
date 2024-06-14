from django.shortcuts import render
import random


def index(request):
    def get_user_choice():
        choice = input("请输入你的选择(石头、剪刀、布): ")
        while choice not in ["石头", "剪刀", "布"]:
            choice = input("输入错误，请重新输入(石头、剪刀、布): ")
        return choice

    def get_computer_choice():
        choices = ["石头", "剪刀", "布"]
        return random.choice(choices)

    def determine_winner(user_choice, computer_choice):
        if user_choice == computer_choice:
            return "平局!"
        elif (user_choice == "石头" and computer_choice == "剪刀") or \
                (user_choice == "剪刀" and computer_choice == "布") or \
                (user_choice == "布" and computer_choice == "石头"):
            return "你赢了!"
        else:
            return "你输了!"