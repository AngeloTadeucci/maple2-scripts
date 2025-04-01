""" trigger/66200001_gd/color_7410.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='Color41', value=10)
        self.set_mesh(trigger_ids=[841], visible=True) # yellow
        self.set_mesh(trigger_ids=[941]) # green
        self.set_mesh(trigger_ids=[1041]) # red

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ColorStart') == 1:
            return YellowBefore(self.ctx)


# Yellow Before
class YellowBefore(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[841], visible=True, fade=2.0) # yellow
        self.set_mesh(trigger_ids=[941]) # green
        self.set_mesh(trigger_ids=[1041]) # red

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ColorClear') == 1:
            return Clear(self.ctx)
        if self.user_value(key='ColorReset') == 1:
            return Reset(self.ctx)
        if self.user_value(key='ColorEnd') == 1:
            return Regen(self.ctx)
        if self.user_value(key='Color41') == 2:
            return GreenAfter(self.ctx)
        if self.user_value(key='Color41') == 3:
            return None # Missing State: YellowtoRed


# Red Before
class RedBefore(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[1041], visible=True) # red
        self.set_mesh(trigger_ids=[941]) # green
        self.set_mesh(trigger_ids=[841]) # yellow

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ColorClear') == 1:
            return Clear(self.ctx)
        if self.user_value(key='ColorReset') == 1:
            return Reset(self.ctx)
        if self.user_value(key='ColorEnd') == 1:
            return Regen(self.ctx)
        if self.user_value(key='Color41') == 1:
            return YellowAfter(self.ctx)
        if self.user_value(key='Color41') == 2:
            return GreenAfter(self.ctx)


# Green After
class GreenAfter(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[941], visible=True) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ColorClear') == 1:
            return Clear(self.ctx)
        if self.user_value(key='ColorReset') == 1:
            return Reset(self.ctx)
        if self.user_value(key='ColorEnd') == 1:
            return Regen(self.ctx)
        if self.user_value(key='Color41') == 1:
            return YellowAfter(self.ctx)
        if self.user_value(key='Color41') == 3:
            return RedAfter(self.ctx)


# Yellow After
class YellowAfter(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[841], visible=True, fade=2.0) # yellow
        self.set_mesh(trigger_ids=[941]) # green
        self.set_mesh(trigger_ids=[1041], start_delay=100) # red

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ColorClear') == 1:
            return Clear(self.ctx)
        if self.user_value(key='ColorReset') == 1:
            return Reset(self.ctx)
        if self.user_value(key='ColorEnd') == 1:
            return Regen(self.ctx)
        if self.user_value(key='Color41') == 2:
            return GreenAfter(self.ctx)
        if self.user_value(key='Color41') == 3:
            return RedAfter(self.ctx)


# Red After
class RedAfter(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[1041], visible=True) # red
        self.set_mesh(trigger_ids=[941]) # green
        self.set_mesh(trigger_ids=[841], start_delay=100) # yellow

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ColorClear') == 1:
            return Clear(self.ctx)
        if self.user_value(key='ColorReset') == 1:
            return Reset(self.ctx)
        if self.user_value(key='ColorEnd') == 1:
            return Regen(self.ctx)
        if self.user_value(key='Color41') == 1:
            return YellowAfter(self.ctx)
        if self.user_value(key='Color41') == 2:
            return GreenAfter(self.ctx)


# All Clear
class Clear(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[941], fade=2.0) # green
        self.set_mesh(trigger_ids=[841], fade=2.0) # yellow
        self.set_mesh(trigger_ids=[1041], fade=2.0) # red

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ColorEnd') == 1:
            return Regen(self.ctx)


# Regen
class Regen(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='ColorStart', value=0) # Pattern Trigger
        self.set_user_value(key='ColorEnd', value=0) # Main Trigger
        self.set_user_value(key='ColorReset', value=0) # Sensor Trigger
        self.set_user_value(key='ColorClear', value=0) # Sensor Trigger
        self.set_mesh(trigger_ids=[841], visible=True, start_delay=400) # yellow
        self.set_mesh(trigger_ids=[941]) # green
        self.set_mesh(trigger_ids=[1041]) # red

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Wait(self.ctx)


# Reset
class Reset(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='ColorStart', value=0) # Pattern Trigger
        self.set_user_value(key='ColorReset', value=0) # Sensor Trigger
        self.set_user_value(key='ColorClear', value=0) # Sensor Trigger

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ColorEnd') == 1:
            return Wait(self.ctx)

    def on_exit(self) -> None:
        self.set_user_value(key='ColorEnd', value=0) # Main Trigger


initial_state = Wait
