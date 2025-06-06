""" trigger/02020141_bf/mobspawn12.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return 보스등장때까지잠시대기(self.ctx)


class 보스등장때까지잠시대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            # 아래 단계 <condition name="몬스터가죽어있으면" arg1="99"> 트리거가 정상 체크 되려면, main.xml 트리거쪽에서 보스가 등장한 이후 진행되어야 하기 때문에, main.xml 트리거쪽에서 보스 등장때까지 잠시 WaitTick 대기함
            return 트리거영역체크시작(self.ctx)


class 트리거영역체크시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='MobSpawnStop') == 4:
            # 보스 HP가 기준 이하가 되면, 졸몹 등장 로직 정지, AI_TurkaHoodForce_Phase03.xml 에서 MobSpawnStop = 4 신호를 이 트리거에 보내서 작동 정지 시킴
            return 졸몬스터제거작업(self.ctx)
        # ##  보스가 죽으면 졸몹 등장 트리거 종료시키기 ##
        if self.monster_dead(spawn_ids=[99]):
            # 보스가 죽으면, 졸몹 등장 로직 정지
            return 졸몬스터제거작업(self.ctx)
        if self.user_detected(box_ids=[11200]):
            # MS2TriggerBox   TriggerObjectID = 11200, 이 트리거 박스 안에 플레이어가 한명이라도 체크 되면, 1시 지점에 설치된 트리거 박스
            return 졸몬스터등장대기중(self.ctx)


class 졸몬스터등장대기중(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            # 플레이어가 트리거 영역에 잠깐 들어가다나 나올 경우에는 졸몹 등장하지 않고, 지속적으로 계속 트리거 영역에 있어야 졸몹 등장시키기 위해 waitTick 2~3초 대기 요소 넣음
            return 트리거영역안플레이어최종체크(self.ctx)


class 트리거영역안플레이어최종체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='MobSpawnStop') == 4:
            # 보스 HP가 기준 이하가 되면, 졸몹 등장 로직 정지
            return 졸몬스터제거작업(self.ctx)
        # ##  보스가 죽으면 졸몹 등장 트리거 종료시키기 ##
        if self.monster_dead(spawn_ids=[99]):
            return 졸몬스터제거작업(self.ctx)
        # waitTick 후에도 플레이어가 트리거 박스 안에서 벗어났으면, 다시 처음단계로 돌아가기
        if self.user_detected(box_ids=[11200]):
            # MS2TriggerBox   TriggerObjectID = 11200, 이 트리거 박스 안에 플레이어가 한명이라도 체크 되면, 1시 지점에 설치된 트리거 박스
            return 졸몬스터등장하기(self.ctx)
        if self.wait_tick(wait_tick=500):
            # 이 트리거 단계에서, 플레이어가 트리거 박스에 벗어났다면 다시 처음 단계로 돌아가기
            return 트리거영역체크시작(self.ctx)


class 졸몬스터등장하기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[11201,11202,11203,11204], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            # waitTick 2초 정도 여기 머물게 하여, 혹시 플레이어가 졸몹 등장하자마자 트리거 박스에 벗어나면 졸몹이 등장 즉시 바로 사라지는 어색한 상황이 생길 수 있어서 waitTick 넣음
            return 트리거영역에계속있는지체크(self.ctx)


class 트리거영역에계속있는지체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='MobSpawnStop') == 4:
            # 보스 HP가 기준 이하가 되면, 졸몹 등장 로직 정지
            return 졸몬스터제거작업(self.ctx)
        # ##  보스가 죽으면 졸몹 등장 트리거 종료시키기 ##
        if self.monster_dead(spawn_ids=[99]):
            return 졸몬스터제거작업(self.ctx)
        if self.user_detected(box_ids=[11200]):
            # MS2TriggerBox   TriggerObjectID = 11200, 이 트리거 박스 안에 플레이어가 한명이라도 체크 되면, 1시 지점에 설치된 트리거 박스
            return 졸몬스터리젠단계시작(self.ctx)
        if not self.user_detected(box_ids=[11200]):
            # MS2TriggerBox   TriggerObjectID = 11200, 이 트리거 박스에 플레어어가 나가게 되면
            return 졸몬스터제거작동대기(self.ctx)


class 졸몬스터리젠단계시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[11200]):
            # MS2TriggerBox   TriggerObjectID = 11200, 이 트리거 박스 안에 플레이어가 한명이라도 체크 되면, 1시 지점에 설치된 트리거 박스
            return 졸몬스터리젠대기중(self.ctx)
        if not self.user_detected(box_ids=[11200]):
            # MS2TriggerBox   TriggerObjectID = 11200, 이 트리거 박스에 플레어어가 나가게 되면
            return 졸몬스터제거작동대기(self.ctx)


class 졸몬스터리젠대기중(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='MobSpawnStop') == 4:
            # 보스 HP가 기준 이하가 되면, 졸몹 등장 로직 정지
            return 졸몬스터제거작업(self.ctx)
        # ##  보스가 죽으면 졸몹 등장 트리거 종료시키기 ##
        if self.monster_dead(spawn_ids=[99]):
            return 졸몬스터제거작업(self.ctx)
        if not self.user_detected(box_ids=[11200]):
            # MS2TriggerBox   TriggerObjectID = 11200, 이 트리거 박스에 플레어어가 나가게 되면
            return 졸몬스터제거작동대기(self.ctx)
        if self.wait_tick(wait_tick=15000):
            # WaitTick 시간 지날때 마다 계속 리젠시킴, AI쪽에서 시간 지나면 스스로 제거시키기 때문에 무한 증식은 안됨
            return 졸몬스터리젠YesNo(self.ctx)


class 졸몬스터리젠YesNo(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='MobSpawnStop') == 4:
            # 보스 HP가 기준 이하가 되면, 졸몹 등장 로직 정지
            return 졸몬스터제거작업(self.ctx)
        # ##  보스가 죽으면 졸몹 등장 트리거 종료시키기 ##
        if self.monster_dead(spawn_ids=[99]):
            return 졸몬스터제거작업(self.ctx)
        if self.user_detected(box_ids=[11200]):
            # MS2TriggerBox   TriggerObjectID = 11200, 이 트리거 박스 안에 플레이어가 한명이라도 체크 되면, 1시 지점에 설치된 트리거 박스
            return 졸몬스터등장하기(self.ctx)
        if not self.user_detected(box_ids=[11200]):
            # MS2TriggerBox   TriggerObjectID = 11200, 이 트리거 박스에 플레어어가 나가게 되면
            return 졸몬스터제거작동대기(self.ctx)


class 졸몬스터제거작동대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[11200]):
            # MS2TriggerBox   TriggerObjectID = 11200 트리거 영역에 잠깐 벗어나 있다가 바로 들어오면, 이전 단계로 돌아가도록 하기
            return 트리거영역에계속있는지체크(self.ctx)
        if self.wait_tick(wait_tick=7000):
            # 트리거 영역에 벗어나자마자 바로 졸몬스터 제거하면 어색한 상황이 생기기 때문에, WaitTick 7초 동안 트리거 영역에 벗어나있는지 체크되면 이때 졸 몬스터 제거 로직 진행하도록 함
            return 졸몬스터제거작업(self.ctx)


class 졸몬스터제거작업(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[11201,11202,11203,11204])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='MobSpawnStop') == 4:
            # 보스 HP가 기준 이하가 되면, 졸몹 등장 로직 정지, AI_TurkaHoodForce_Phase03.xml 에서 MobSpawnStop = 4 신호를 이 트리거에 보내서 작동 정지 시킴
            return 종료(self.ctx)
        # ##  보스가 죽으면 졸몹 등장 트리거 종료시키기 ##
        if self.monster_dead(spawn_ids=[99]):
            # 보스가 죽으면, 졸몹 등장 로직 정지
            return 종료(self.ctx)
        if self.wait_tick(wait_tick=2000):
            # 졸 몬스터 제거하고 다시 처음 단계로 돌아가기
            return 트리거영역체크시작(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 시작대기중
