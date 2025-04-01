""" trigger/02000376_bf/06_puzzle_secondpiece.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='PickSecondPieceExceptA01', value=0)
        self.set_user_value(key='PickSecondPieceExceptA02', value=0)
        self.set_user_value(key='PickSecondPieceExceptA03', value=0)
        self.set_user_value(key='PickSecondPieceExceptB01', value=0)
        self.set_user_value(key='PickSecondPieceExceptB02', value=0)
        self.set_user_value(key='PickSecondPieceExceptC01', value=0)
        self.set_user_value(key='PickSecondPieceExceptD01', value=0)
        self.set_user_value(key='PickSecondPieceExceptD02', value=0)
        self.set_user_value(key='PickSecondPieceExceptE01', value=0)
        self.set_user_value(key='PickSecondPieceExceptE02', value=0)
        self.set_user_value(key='CheckSecondPiece', value=0)
        self.set_user_value(key='CorrectSecondPiece', value=0)
        self.set_user_value(key='ResetSecondPiece', value=0)
        self.set_user_value(key='LockSecondPiece', value=0)
        self.set_mesh(trigger_ids=[3200,3201,3202,3203,3204,3205,3206,3207,3208,3209]) # Pattern_Ground
        self.set_mesh(trigger_ids=[3210,3211,3212,3213,3214,3215,3216,3217,3218,3219]) # Pattern_LightOn

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='PickSecondPieceExceptA01') == 1:
            return RandomPick_ExceptA01(self.ctx)
        if self.user_value(key='PickSecondPieceExceptA02') == 1:
            return RandomPick_ExceptA02(self.ctx)
        if self.user_value(key='PickSecondPieceExceptA03') == 1:
            return RandomPick_ExceptA03(self.ctx)
        if self.user_value(key='PickSecondPieceExceptB01') == 1:
            return RandomPick_ExceptB01(self.ctx)
        if self.user_value(key='PickSecondPieceExceptB02') == 1:
            return RandomPick_ExceptB02(self.ctx)
        if self.user_value(key='PickSecondPieceExceptC01') == 1:
            return RandomPick_ExceptC01(self.ctx)
        if self.user_value(key='PickSecondPieceExceptD01') == 1:
            return RandomPick_ExceptD01(self.ctx)
        if self.user_value(key='PickSecondPieceExceptD02') == 1:
            return RandomPick_ExceptD02(self.ctx)
        if self.user_value(key='PickSecondPieceExceptE01') == 1:
            return RandomPick_ExceptE01(self.ctx)
        if self.user_value(key='PickSecondPieceExceptE02') == 1:
            return RandomPick_ExceptE02(self.ctx)


class RandomPick_ExceptA01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=10.0):
            return Pattern02_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern03_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern04_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern05_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern06_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern07_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern08_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern09_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern10_Pick(self.ctx)


class RandomPick_ExceptA02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=10.0):
            return Pattern01_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern03_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern04_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern05_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern06_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern07_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern08_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern09_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern10_Pick(self.ctx)


class RandomPick_ExceptA03(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=10.0):
            return Pattern01_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern02_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern04_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern05_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern06_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern07_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern08_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern09_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern10_Pick(self.ctx)


class RandomPick_ExceptB01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=10.0):
            return Pattern01_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern02_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern03_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern05_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern06_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern07_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern08_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern09_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern10_Pick(self.ctx)


class RandomPick_ExceptB02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=10.0):
            return Pattern01_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern02_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern03_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern04_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern06_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern07_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern08_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern09_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern10_Pick(self.ctx)


class RandomPick_ExceptC01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=10.0):
            return Pattern01_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern02_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern03_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern04_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern05_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern07_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern08_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern09_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern10_Pick(self.ctx)


class RandomPick_ExceptD01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=10.0):
            return Pattern01_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern02_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern03_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern04_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern05_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern06_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern08_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern09_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern10_Pick(self.ctx)


class RandomPick_ExceptD02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=10.0):
            return Pattern01_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern02_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern03_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern04_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern05_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern06_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern07_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern09_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern10_Pick(self.ctx)


class RandomPick_ExceptE01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=10.0):
            return Pattern01_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern02_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern03_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern04_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern05_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern06_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern07_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern08_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern10_Pick(self.ctx)


class RandomPick_ExceptE02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=10.0):
            return Pattern01_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern02_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern03_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern04_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern05_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern06_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern07_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern08_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern09_Pick(self.ctx)


# 첫 번째 패턴 뽑힘
class Pattern01_Pick(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3200], visible=True) # Pattern_Ground_A01

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CheckSecondPiece') == 1:
            return Pattern01_Check(self.ctx)


# 첫 번째 패턴 정답 체크
class Pattern01_Check(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[2002], item_id=30000565):
            # Pattern_A01
            return Pattern01_CorrectAnswer(self.ctx)
        if not self.detect_liftable_object(box_ids=[2002], item_id=30000565):
            # 돌이 없거나 정답이 아니면
            return Pattern01_WrongAnswer(self.ctx)


# 첫 번째 패턴 정답
class Pattern01_CorrectAnswer(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=4, key='CorrectSecondPiece', value=1) # 정답
        self.set_mesh(trigger_ids=[3210], visible=True, start_delay=100, fade=5.0) # Pattern_LightOn_A01

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ResetSecondPiece') == 1:
            return Pattern01_Reset01(self.ctx)
        if self.user_value(key='LockSecondPiece') == 1:
            return Quit(self.ctx)


# 첫 번째 패턴 오답
class Pattern01_WrongAnswer(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=4, key='CorrectSecondPiece', value=2) # 오답

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Pattern01_Reset01(self.ctx)


class Pattern01_Reset01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='CheckSecondPiece', value=0)
        self.set_user_value(key='CorrectSecondPiece', value=0)
        self.set_user_value(key='ResetSecondPiece', value=0)
        self.set_user_value(key='LockSecondPiece', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Pattern01_Reset02(self.ctx)


# 첫 번째 패턴 다시체크
class Pattern01_Reset02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3210], start_delay=100, fade=5.0) # Pattern_LightOn_A01

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CheckSecondPiece') == 1:
            return Pattern01_Check(self.ctx)


# 두 번째 패턴 뽑힘
class Pattern02_Pick(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3201], visible=True) # Pattern_Ground_A02

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CheckSecondPiece') == 1:
            return Pattern02_Check(self.ctx)


# 두 번째 패턴 정답 체크
class Pattern02_Check(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[2002], item_id=30000566):
            # Pattern_A02
            return Pattern02_CorrectAnswer(self.ctx)
        if not self.detect_liftable_object(box_ids=[2002], item_id=30000566):
            # 돌이 없거나 정답이 아니면
            return Pattern02_WrongAnswer(self.ctx)


# 두 번째 패턴 정답
class Pattern02_CorrectAnswer(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=4, key='CorrectSecondPiece', value=1) # 정답
        self.set_mesh(trigger_ids=[3211], visible=True, start_delay=100, fade=5.0) # Pattern_LightOn_A02

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ResetSecondPiece') == 1:
            return Pattern02_Reset01(self.ctx)
        if self.user_value(key='LockSecondPiece') == 1:
            return Quit(self.ctx)


# 두 번째 패턴 오답
class Pattern02_WrongAnswer(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=4, key='CorrectSecondPiece', value=2) # 오답

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Pattern02_Reset01(self.ctx)


class Pattern02_Reset01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='CheckSecondPiece', value=0)
        self.set_user_value(key='CorrectSecondPiece', value=0)
        self.set_user_value(key='ResetSecondPiece', value=0)
        self.set_user_value(key='LockSecondPiece', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Pattern02_Reset02(self.ctx)


# 두 번째 패턴 다시체크
class Pattern02_Reset02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3211], start_delay=100, fade=5.0) # Pattern_LightOn_A02

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CheckSecondPiece') == 1:
            return Pattern02_Check(self.ctx)


# 세 번째 패턴 뽑힘
class Pattern03_Pick(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3202], visible=True) # Pattern_Ground_A03

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CheckSecondPiece') == 1:
            return Pattern03_Check(self.ctx)


# 세 번째 패턴 정답 체크
class Pattern03_Check(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[2002], item_id=30000567):
            # Pattern_A03
            return Pattern03_CorrectAnswer(self.ctx)
        if not self.detect_liftable_object(box_ids=[2002], item_id=30000567):
            # 돌이 없거나 정답이 아니면
            return Pattern03_WrongAnswer(self.ctx)


# 세 번째 패턴 정답
class Pattern03_CorrectAnswer(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=4, key='CorrectSecondPiece', value=1) # 정답
        self.set_mesh(trigger_ids=[3212], visible=True, start_delay=100, fade=5.0) # Pattern_LightOn_A03

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ResetSecondPiece') == 1:
            return Pattern03_Reset01(self.ctx)
        if self.user_value(key='LockSecondPiece') == 1:
            return Quit(self.ctx)


# 세 번째 패턴 오답
class Pattern03_WrongAnswer(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=4, key='CorrectSecondPiece', value=2) # 오답

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Pattern03_Reset01(self.ctx)


class Pattern03_Reset01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='CheckSecondPiece', value=0)
        self.set_user_value(key='CorrectSecondPiece', value=0)
        self.set_user_value(key='ResetSecondPiece', value=0)
        self.set_user_value(key='LockSecondPiece', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Pattern03_Reset02(self.ctx)


# 세 번째 패턴 다시체크
class Pattern03_Reset02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3212], start_delay=100, fade=5.0) # Pattern_LightOn_A03

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CheckSecondPiece') == 1:
            return Pattern03_Check(self.ctx)


# 네 번째 패턴 뽑힘
class Pattern04_Pick(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3203], visible=True) # Pattern_Ground_B01

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CheckSecondPiece') == 1:
            return Pattern04_Check(self.ctx)


# 네 번째 패턴 정답 체크
class Pattern04_Check(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[2002], item_id=30000568):
            # Pattern_B01
            return Pattern04_CorrectAnswer(self.ctx)
        if not self.detect_liftable_object(box_ids=[2002], item_id=30000568):
            # 돌이 없거나 정답이 아니면
            return Pattern04_WrongAnswer(self.ctx)


# 네 번째 패턴 정답
class Pattern04_CorrectAnswer(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=4, key='CorrectSecondPiece', value=1) # 정답
        self.set_mesh(trigger_ids=[3213], visible=True, start_delay=100, fade=5.0) # Pattern_LightOn_B01

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ResetSecondPiece') == 1:
            return Pattern04_Reset01(self.ctx)
        if self.user_value(key='LockSecondPiece') == 1:
            return Quit(self.ctx)


# 네 번째 패턴 오답
class Pattern04_WrongAnswer(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=4, key='CorrectSecondPiece', value=2) # 오답

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Pattern04_Reset01(self.ctx)


class Pattern04_Reset01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='CheckSecondPiece', value=0)
        self.set_user_value(key='CorrectSecondPiece', value=0)
        self.set_user_value(key='ResetSecondPiece', value=0)
        self.set_user_value(key='LockSecondPiece', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Pattern04_Reset02(self.ctx)


# 네 번째 패턴 다시체크
class Pattern04_Reset02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3213], start_delay=100, fade=5.0) # Pattern_LightOn_B01

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CheckSecondPiece') == 1:
            return Pattern04_Check(self.ctx)


# 다섯 번째 패턴 뽑힘
class Pattern05_Pick(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3204], visible=True) # Pattern_Ground_B02

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CheckSecondPiece') == 1:
            return Pattern05_Check(self.ctx)


# 다섯 번째 패턴 정답 체크
class Pattern05_Check(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[2002], item_id=30000569):
            # Pattern_B02
            return Pattern05_CorrectAnswer(self.ctx)
        if not self.detect_liftable_object(box_ids=[2002], item_id=30000569):
            # 돌이 없거나 정답이 아니면
            return Pattern05_WrongAnswer(self.ctx)


# 다섯 번째 패턴 정답
class Pattern05_CorrectAnswer(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=4, key='CorrectSecondPiece', value=1) # 정답
        self.set_mesh(trigger_ids=[3214], visible=True, start_delay=100, fade=5.0) # Pattern_LightOn_B02

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ResetSecondPiece') == 1:
            return Pattern05_Reset01(self.ctx)
        if self.user_value(key='LockSecondPiece') == 1:
            return Quit(self.ctx)


# 다섯 번째 패턴 오답
class Pattern05_WrongAnswer(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=4, key='CorrectSecondPiece', value=2) # 오답

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Pattern05_Reset01(self.ctx)


class Pattern05_Reset01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='CheckSecondPiece', value=0)
        self.set_user_value(key='CorrectSecondPiece', value=0)
        self.set_user_value(key='ResetSecondPiece', value=0)
        self.set_user_value(key='LockSecondPiece', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Pattern05_Reset02(self.ctx)


# 다섯 번째 패턴 다시체크
class Pattern05_Reset02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3214], start_delay=100, fade=5.0) # Pattern_LightOn_B02

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CheckSecondPiece') == 1:
            return Pattern05_Check(self.ctx)


# 여섯 번째 패턴 뽑힘
class Pattern06_Pick(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3205], visible=True) # Pattern_Ground_C01

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CheckSecondPiece') == 1:
            return Pattern06_Check(self.ctx)


# 여섯 번째 패턴 정답 체크
class Pattern06_Check(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[2002], item_id=30000570):
            # Pattern_C01
            return Pattern06_CorrectAnswer(self.ctx)
        if not self.detect_liftable_object(box_ids=[2002], item_id=30000570):
            # 돌이 없거나 정답이 아니면
            return Pattern06_WrongAnswer(self.ctx)


# 여섯 번째 패턴 정답
class Pattern06_CorrectAnswer(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=4, key='CorrectSecondPiece', value=1) # 정답
        self.set_mesh(trigger_ids=[3215], visible=True, start_delay=100, fade=5.0) # Pattern_LightOn_C01

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ResetSecondPiece') == 1:
            return Pattern06_Reset01(self.ctx)
        if self.user_value(key='LockSecondPiece') == 1:
            return Quit(self.ctx)


# 여섯 번째 패턴 오답
class Pattern06_WrongAnswer(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=4, key='CorrectSecondPiece', value=2) # 오답

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Pattern06_Reset01(self.ctx)


class Pattern06_Reset01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='CheckSecondPiece', value=0)
        self.set_user_value(key='CorrectSecondPiece', value=0)
        self.set_user_value(key='ResetSecondPiece', value=0)
        self.set_user_value(key='LockSecondPiece', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Pattern06_Reset02(self.ctx)


# 여섯 번째 패턴 다시체크
class Pattern06_Reset02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3215], start_delay=100, fade=5.0) # Pattern_LightOn_C01

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CheckSecondPiece') == 1:
            return Pattern06_Check(self.ctx)


# 일곱 번째 패턴 뽑힘
class Pattern07_Pick(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3206], visible=True) # Pattern_Ground_D01

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CheckSecondPiece') == 1:
            return Pattern07_Check(self.ctx)


# 일곱 번째 패턴 정답 체크
class Pattern07_Check(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[2002], item_id=30000571):
            # Pattern_D01
            return Pattern07_CorrectAnswer(self.ctx)
        if not self.detect_liftable_object(box_ids=[2002], item_id=30000571):
            # 돌이 없거나 정답이 아니면
            return Pattern07_WrongAnswer(self.ctx)


# 일곱 번째 패턴 정답
class Pattern07_CorrectAnswer(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=4, key='CorrectSecondPiece', value=1) # 정답
        self.set_mesh(trigger_ids=[3216], visible=True, start_delay=100, fade=5.0) # Pattern_LightOn_D01

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ResetSecondPiece') == 1:
            return Pattern07_Reset01(self.ctx)
        if self.user_value(key='LockSecondPiece') == 1:
            return Quit(self.ctx)


# 일곱 번째 패턴 오답
class Pattern07_WrongAnswer(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=4, key='CorrectSecondPiece', value=2) # 오답

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Pattern07_Reset01(self.ctx)


class Pattern07_Reset01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='CheckSecondPiece', value=0)
        self.set_user_value(key='CorrectSecondPiece', value=0)
        self.set_user_value(key='ResetSecondPiece', value=0)
        self.set_user_value(key='LockSecondPiece', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Pattern07_Reset02(self.ctx)


# 일곱 번째 패턴 다시체크
class Pattern07_Reset02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3216], start_delay=100, fade=5.0) # Pattern_LightOn_D01

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CheckSecondPiece') == 1:
            return Pattern07_Check(self.ctx)


# 여덟 번째 패턴 뽑힘
class Pattern08_Pick(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3207], visible=True) # Pattern_Ground_D02

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CheckSecondPiece') == 1:
            return Pattern08_Check(self.ctx)


# 여덟 번째 패턴 정답 체크
class Pattern08_Check(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[2002], item_id=30000572):
            # Pattern_D02
            return Pattern08_CorrectAnswer(self.ctx)
        if not self.detect_liftable_object(box_ids=[2002], item_id=30000572):
            # 돌이 없거나 정답이 아니면
            return Pattern08_WrongAnswer(self.ctx)


# 여덟 번째 패턴 정답
class Pattern08_CorrectAnswer(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=4, key='CorrectSecondPiece', value=1) # 정답
        self.set_mesh(trigger_ids=[3217], visible=True, start_delay=100, fade=5.0) # Pattern_LightOn_D02

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ResetSecondPiece') == 1:
            return Pattern08_Reset01(self.ctx)
        if self.user_value(key='LockSecondPiece') == 1:
            return Quit(self.ctx)


# 여덟 번째 패턴 오답
class Pattern08_WrongAnswer(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=4, key='CorrectSecondPiece', value=2) # 오답

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Pattern08_Reset01(self.ctx)


class Pattern08_Reset01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='CheckSecondPiece', value=0)
        self.set_user_value(key='CorrectSecondPiece', value=0)
        self.set_user_value(key='ResetSecondPiece', value=0)
        self.set_user_value(key='LockSecondPiece', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Pattern08_Reset02(self.ctx)


# 여덟 번째 패턴 다시체크
class Pattern08_Reset02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3217], start_delay=100, fade=5.0) # Pattern_LightOn_D02

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CheckSecondPiece') == 1:
            return Pattern08_Check(self.ctx)


# 아홉 번째 패턴 뽑힘
class Pattern09_Pick(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3208], visible=True) # Pattern_Ground_E01

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CheckSecondPiece') == 1:
            return Pattern09_Check(self.ctx)


# 아홉 번째 패턴 정답 체크
class Pattern09_Check(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[2002], item_id=30000573):
            # Pattern_E01
            return Pattern09_CorrectAnswer(self.ctx)
        if not self.detect_liftable_object(box_ids=[2002], item_id=30000573):
            # 돌이 없거나 정답이 아니면
            return Pattern09_WrongAnswer(self.ctx)


# 아홉 번째 패턴 정답
class Pattern09_CorrectAnswer(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=4, key='CorrectSecondPiece', value=1) # 정답
        self.set_mesh(trigger_ids=[3218], visible=True, start_delay=100, fade=5.0) # Pattern_LightOn_E01

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ResetSecondPiece') == 1:
            return Pattern09_Reset01(self.ctx)
        if self.user_value(key='LockSecondPiece') == 1:
            return Quit(self.ctx)


# 아홉 번째 패턴 오답
class Pattern09_WrongAnswer(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=4, key='CorrectSecondPiece', value=2) # 오답

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Pattern09_Reset01(self.ctx)


class Pattern09_Reset01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='CheckSecondPiece', value=0)
        self.set_user_value(key='CorrectSecondPiece', value=0)
        self.set_user_value(key='ResetSecondPiece', value=0)
        self.set_user_value(key='LockSecondPiece', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Pattern09_Reset02(self.ctx)


# 아홉 번째 패턴 다시체크
class Pattern09_Reset02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3218], start_delay=100, fade=5.0) # Pattern_LightOn_E01

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CheckSecondPiece') == 1:
            return Pattern09_Check(self.ctx)


# 열 번째 패턴 뽑힘
class Pattern10_Pick(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3209], visible=True) # Pattern_Ground_E02

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CheckSecondPiece') == 1:
            return Pattern10_Check(self.ctx)


# 열 번째 패턴 정답 체크
class Pattern10_Check(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[2002], item_id=30000574):
            # Pattern_E02
            return Pattern10_CorrectAnswer(self.ctx)
        if not self.detect_liftable_object(box_ids=[2002], item_id=30000574):
            # 돌이 없거나 정답이 아니면
            return Pattern10_WrongAnswer(self.ctx)


# 열 번째 패턴 정답
class Pattern10_CorrectAnswer(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=4, key='CorrectSecondPiece', value=1) # 정답
        self.set_mesh(trigger_ids=[3219], visible=True, start_delay=100, fade=5.0) # Pattern_LightOn_E02

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ResetSecondPiece') == 1:
            return Pattern10_Reset01(self.ctx)
        if self.user_value(key='LockSecondPiece') == 1:
            return Quit(self.ctx)


# 열 번째 패턴 오답
class Pattern10_WrongAnswer(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=4, key='CorrectSecondPiece', value=2) # 오답

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Pattern10_Reset01(self.ctx)


class Pattern10_Reset01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='CheckSecondPiece', value=0)
        self.set_user_value(key='CorrectSecondPiece', value=0)
        self.set_user_value(key='ResetSecondPiece', value=0)
        self.set_user_value(key='LockSecondPiece', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Pattern10_Reset02(self.ctx)


# 열 번째 패턴 다시체크
class Pattern10_Reset02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3219], start_delay=100, fade=5.0) # Pattern_LightOn_E02

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CheckSecondPiece') == 1:
            return Pattern10_Check(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
