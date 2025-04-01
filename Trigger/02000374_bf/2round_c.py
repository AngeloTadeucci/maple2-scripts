""" trigger/02000374_bf/2round_c.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='2Round_C') == 1:
            return Spawn_Start_Ready(self.ctx)


class Spawn_Start_Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Spawn_Start(self.ctx)


class Spawn_Start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7101], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return Round_Spawn_C_01_Ready2(self.ctx)


class Round_Spawn_C_01_Ready2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7201], visible=True)
        self.set_effect(trigger_ids=[7001])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2300):
            # 스폰 타이밍
            return Round_Spawn_C_01_2(self.ctx)


class Round_Spawn_C_01_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[104], auto_target=False) # 데블린 치프 등장

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[104]):
            return Round_Spawn_C_End2(self.ctx)


class Round_Spawn_C_End2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=110, patrol_name='MS2PatrolData_2008')
        self.set_dialogue(type=1, spawn_id=110, script='$02000374_BF__2ROUND_C__0$', time=2, arg5=1)
        self.set_user_value(trigger_id=2037401, key='2Round_C', value=1) # 데블린 치프  소환 장치


initial_state = idle
