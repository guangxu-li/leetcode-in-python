#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#


# @lc code=start
class DFA:
    STATE_END = 0
    STATE_INIT = 1
    STATE_POSITIVE = 2
    STATE_NEGATIVE = 3
    STATE_NUMBER = 4

    SIGNAL_OTHER = 0
    SIGNAL_SPACE = 1
    SIGNAL_PLUS = 2
    SIGNAL_MINUS = 3
    SIGNAL_DIGIT = 4

    def __init__(self):
        self.last_state = self.STATE_END
        self.state = self.STATE_INIT
        self.transition = {
            self.STATE_END: {
                self.SIGNAL_OTHER: self.STATE_END,
                self.SIGNAL_SPACE: self.STATE_END,
                self.SIGNAL_PLUS: self.STATE_END,
                self.SIGNAL_MINUS: self.STATE_END,
                self.SIGNAL_DIGIT: self.STATE_END,
            },
            self.STATE_INIT: {
                self.SIGNAL_OTHER: self.STATE_END,
                self.SIGNAL_SPACE: self.STATE_INIT,
                self.SIGNAL_PLUS: self.STATE_POSITIVE,
                self.SIGNAL_MINUS: self.STATE_NEGATIVE,
                self.SIGNAL_DIGIT: self.STATE_NUMBER,
            },
            self.STATE_POSITIVE: {
                self.SIGNAL_OTHER: self.STATE_END,
                self.SIGNAL_SPACE: self.STATE_END,
                self.SIGNAL_PLUS: self.STATE_END,
                self.SIGNAL_MINUS: self.STATE_END,
                self.SIGNAL_DIGIT: self.STATE_NUMBER,
            },
            self.STATE_NEGATIVE: {
                self.SIGNAL_OTHER: self.STATE_END,
                self.SIGNAL_SPACE: self.STATE_END,
                self.SIGNAL_PLUS: self.STATE_END,
                self.SIGNAL_MINUS: self.STATE_END,
                self.SIGNAL_DIGIT: self.STATE_NUMBER,
            },
            self.STATE_NUMBER: {
                self.SIGNAL_OTHER: self.STATE_END,
                self.SIGNAL_SPACE: self.STATE_END,
                self.SIGNAL_PLUS: self.STATE_END,
                self.SIGNAL_MINUS: self.STATE_END,
                self.SIGNAL_DIGIT: self.STATE_NUMBER,
            },
        }

    def signal(self, ch: str) -> int:
        if ch == " ":
            return self.SIGNAL_SPACE
        elif ch == "+":
            return self.SIGNAL_PLUS
        elif ch == "-":
            return self.SIGNAL_MINUS
        elif ch.isdigit():
            return self.SIGNAL_DIGIT
        else:
            return self.SIGNAL_OTHER

    def transit(self, ch: str):
        self.last_state = self.state
        self.state = self.transition[self.state][self.signal(ch)]
        return self.last_state, self.state


class Solution:
    def myAtoi(self, s: str) -> int:
        num, dfa, positive = 0, DFA(), True
        for ch in s:
            last_state, state = dfa.transit(ch)
            if state == DFA.STATE_END:
                break
            if state == DFA.STATE_INIT:
                continue
            elif state == DFA.STATE_NEGATIVE:
                positive = False
            elif state == DFA.STATE_POSITIVE:
                continue
            else:
                digit = ord(ch) - ord("0")
                if num > 2**31 // 10 or (num == 2**31 // 10 and digit > 2**31 % 10 - int(positive)):
                    return 2**31 - 1 if positive else -(2**31)
                num = num * 10 + digit

        return num if positive else -num


# @lc code=end
