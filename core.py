from hub import light_matrix
import runloop, time

    # https://spike3-docs.web.app/?page=Modules%20hub.motion_sensor
async def main():
    # write your code here
    await light_matrix.write("Hi MayanK!")

    from hub import motion_sensor
    while True:
        # time.sleep(3)
        list_motion = ['BACK', 'BOTTOM', 'DOUBLE_TAPPED', 'FALLING', 'FRONT', 'LEFT', 'RIGHT', 'SHAKEN', 'TAPPED', 'TOP', 'UNKNOWN', 'acceleration', 'angular_velocity', 'gesture', 'get_yaw_face', 'quaternion', 'reset_tap_count', 'reset_yaw', 'set_yaw_face', 'stable', 'tap_count', 'tilt_angles', 'up_face']
   
        for item in list_motion:
            print(
                motion_sensor.BACK,
                motion_sensor.BOTTOM,
                motion_sensor.DOUBLE_TAPPED,
                motion_sensor.FALLING,
                motion_sensor.FRONT,
                motion_sensor.LEFT,
                motion_sensor.RIGHT,
                motion_sensor.SHAKEN,
                motion_sensor.TAPPED,
                motion_sensor.TOP,
                motion_sensor.UNKNOWN,
                motion_sensor.acceleration(),
                motion_sensor.angular_velocity(),
                motion_sensor.gesture(),
                motion_sensor.get_yaw_face(),
                motion_sensor.quaternion(),
                motion_sensor.reset_tap_count(),
                motion_sensor.reset_yaw(),
                # dir(motion_sensor.set_yaw_face()),
                motion_sensor.stable(),
                motion_sensor.tap_count(),
                motion_sensor.tilt_angles(),
                motion_sensor.up_face()
            )

    #['__class__', '__name__', '__dict__', 
    #'battery_current', 
    #'battery_temperature', 
    #'battery_voltage', 
    #'bootloader', 
    #'button', 
    #'config', 
    #'device_uuid', 
    #'hardware_id', 
    #'light', 
    #'light_matrix', 
    ###'motion_sensor', 
    #'port', 
    #'power_off', 
    #'reset', 
    #'soft_reset', 
    #'sound', 
    #'temperature', 
    #'usb_charge_current']
    # import hub
    # print(dir(hub))

    #    ['__class__', '__name__', '__dict__', 
    #'BACK', 'BOTTOM', 'DOUBLE_TAPPED', 'FALLING', 'FRONT', 
    #'LEFT', 'RIGHT', 'SHAKEN', 'TAPPED', 'TOP', 'UNKNOWN', 
    #'acceleration', 'angular_velocity', 'gesture', 'get_yaw_face', 
    #'quaternion', 'reset_tap_count', 'reset_yaw', 'set_yaw_face', 
    #'stable', 'tap_count', 'tilt_angles', 'up_face']
    # print(dir(hub.motion_sensor))

    # ['__class__', '__init__', '__name__', 'stop', '__dict__', 
    #'BRAKE', 'CANCELLED', 'CLOCKWISE', 'COAST', 'CONTINUE', 
    #'COUNTERCLOCKWISE', 'DISCONNECTED', 'ERROR', 'HOLD', 'LONGEST_PATH', 
    #'READY', 'RUNNING', 'SHORTEST_PATH', 'SMART_BRAKE', 'SMART_COAST', 
    #'STALLED', 'absolute_position', 'get_duty_cycle', 'info', 
    #'relative_position', 'reset_relative_position', 'run', 
    #'run_for_degrees', 'run_for_time', 'run_to_absolute_position', 
    #'run_to_relative_position', 'set_duty_cycle', 'status', 'velocity']
    # import motor
    # print(dir(motor))

runloop.run(main())
