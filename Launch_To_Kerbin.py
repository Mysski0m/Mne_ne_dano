## посадка на Кербин (с выбранной целью)

import krpc

conn = krpc.connect(name="Our mission")

sc = conn.space_center
mj = conn.mech_jeb
landing = mj.landing_autopilot

landing.deploy_chutes = True
landing.deploy_gears = True
landing.land_untargeted()
landing.touchdown_speed = 2700
landing.enabled = True

with conn.stream(getattr, landing, "enabled") as enabled:
    enabled.rate = 1 #we don't need a high throughput rate, 1 second is more than enough
    with enabled.condition:
        while enabled():
            enabled.wait()

print("Landing complete!")
conn.close()