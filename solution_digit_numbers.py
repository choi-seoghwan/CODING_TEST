# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 20:40:42 2020

@author: choi
"""

# 입력값(자연수):  1234567
# 결과값(배열 ): [7,6,5,4,3,2,1]

def solution(n):
    answer = []
    string_number = str(n)
    digit_number = len(string_number)
    while digit_number > 0:
        digit_number = digit_number - 1
        answer.append(int(string_number[digit_number]))
    return answer

print(solution(1234567))