## долет до Кербина

import krpc

conn = krpc.connect(name="Our mission")

sc = conn.space_center
mj = conn.mech_jeb

print("Planning return transfer")
planner = mj.maneuver_planner
returnKerbin = planner.operation_moon_return
returnKerbin.moon_return_altitude = 30000
print('return makes nodes')
returnKerbin.make_nodes()
print('creates')

#check for warnings
warning = returnKerbin.error_message
if warning:
    print(warning)

def execute_nodes():
    print("Executing maneuver nodes")
    executor.execute_all_nodes()

    with conn.stream(getattr, executor, "enabled") as enabled:
        enabled.rate = 1  # we don't need a high throughput rate, 1 second is more than enough
        with enabled.condition:
            while enabled():
                enabled.wait()

# execute the nodes
executor = mj.node_executor
execute_nodes()

print("Return complete!")

conn.close()