""" trigger/82000002_survival/09_normalbox.xml """
import trigger_api


"""
다수의 interactObject 동시 스폰하는 경우 렉이 발생함 / 대기 지역에 배치된 나무 상자 그룹만 경기 시작 시점에 스폰 시키는 것으로 구현함
10000040-10000164 나무 상자 Normal Box
"""
class Setting(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_combine_spawn(group_id=[10000382,10000383,10000384,10000385,10000386,10000387,10000388,10000389,10000390,10000391,10000392,10000393,10000394,10000395,10000396,10000397,10000398,10000399,10000400,10000401,10000402,10000403,10000404,10000405,10000406,10000407,10000408,10000409,10000410,10000411,10000412,10000413,10000414,10000415,10000416,10000417,10000418,10000419,10000420,10000421,10000422,10000423,10000424,10000425,10000426,10000427,10000428,10000429,10000430,10000431,10000432,10000433,10000434,10000435], is_start=True)
        self.start_combine_spawn(group_id=[10000440,10000442,10000444,10000445,10000446,10000448,10000449,10000451,10000452], is_start=True)
        self.start_combine_spawn(group_id=[10000454,10000455,10000456,10000457,10000458,10000459,10000460,10000461,10000462,10000463,10000464,10000465,10000466,10000467,10000468,10000469,10000470,10000471,10000472,10000473,10000474,10000475,10000476,10000477,10000478,10000479,10000480,10000481,10000482,10000483,10000484,10000485,10000486,10000487,10000488,10000489,10000490,10000491,10000492,10000493,10000494,10000495,10000496,10000497,10000498,10000499,10000500,10000501,10000502,10000503,10000504,10000505,10000506], is_start=True)
        self.set_user_value(key='NormaBoxOnCount', value=0)
        self.set_user_value(key='NormaBoxOff', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='NormaBoxOnCount') == 1:
            return Delay(self.ctx)


class Delay(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 대기지역을 포함하는 그룹 별도 스폰
        self.start_combine_spawn(group_id=[10000436,10000437,10000438,10000439,10000441,10000443,10000447,10000450,10000453], is_start=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='NormaBoxOff') == 1:
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 10000040-10000506 나무 상자 Normal Box
        self.start_combine_spawn(group_id=[10000382,10000383,10000384,10000385,10000386,10000387,10000388,10000389,10000390,10000391,10000392,10000393,10000394,10000395,10000396,10000397,10000398,10000399,10000400,10000401,10000402,10000403,10000404,10000405,10000406,10000407,10000408,10000409,10000410,10000411,10000412,10000413,10000414,10000415,10000416,10000417,10000418,10000419,10000420,10000421,10000422,10000423,10000424,10000425,10000426,10000427,10000428,10000429,10000430,10000431,10000432,10000433,10000434,10000435,10000436,10000437,10000438,10000439,10000440,10000441,10000442,10000443,10000444,10000445,10000446,10000447,10000448,10000449,10000450,10000451,10000452,10000453,10000454,10000455,10000456,10000457,10000458,10000459,10000460,10000461,10000462,10000463,10000464,10000465,10000466,10000467,10000468,10000469,10000470,10000471,10000472,10000473,10000474,10000475,10000476,10000477,10000478,10000479,10000480,10000481,10000482,10000483,10000484,10000485,10000486,10000487,10000488,10000489,10000490,10000491,10000492,10000493,10000494,10000495,10000496,10000497,10000498,10000499,10000500,10000501,10000502,10000503,10000504,10000505,10000506])


initial_state = Setting
