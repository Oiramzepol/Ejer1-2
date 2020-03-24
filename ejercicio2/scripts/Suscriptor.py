#!/usr/bin/env python
# license removed for brevity 
import rospy
from std_msgs.msg import Int64

def talker():
    
    pub = rospy.Publisher('info_numero', Int64, queue_size=10)
    rospy.init_node('Ismael', anonymous=True) 
    counter=0
    while not rospy.is_shutdown():
        numero=int(input("dame el numero que quieres publicar "))
        rospy.loginfo("el valor introducido es %d",numero)
        pub.publish(numero)

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass 