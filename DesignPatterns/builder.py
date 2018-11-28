from abc import ABC, abstractmethod


class RobotPlan(ABC):
    # defines what every robot has
    @abstractmethod
    def set_robot_head(self, head):
        pass

    @abstractmethod
    def set_robot_torso(self, torso):
        pass

    @abstractmethod
    def set_robot_arms(self, arms):
        pass

    @abstractmethod
    def set_robot_legs(self, legs):
        pass


class Robot(RobotPlan):
    # specific robot
    def __init__(self) -> None:
        self._arms = None
        self._legs = None
        self._head = None
        self._torso = None

    def set_robot_arms(self, arms):
        self._arms = arms

    def get_robot_arms(self):
        return self._arms

    def set_robot_legs(self, legs):
        self._legs = legs

    def get_robot_legs(self):
        return self._legs

    def set_robot_head(self, head):
        self._head = head

    def get_robot_head(self):
        return self._head

    def set_robot_torso(self, torso):
        self._torso = torso

    def get_robot_torso(self):
        return self._torso


class RobotBuilder(ABC):
    # abstract method for constructing any type of robot
    @abstractmethod
    def get_robot(self):
        pass

    @abstractmethod
    def build_robot_head(self):
        pass

    @abstractmethod
    def build_robot_legs(self):
        pass

    @abstractmethod
    def build_robot_torso(self):
        pass

    @abstractmethod
    def build_robot_arms(self):
        pass


class OldRobotBuilder(RobotBuilder):
    # concrete robot builder for a specific type of robot
    def __init__(self) -> None:
        self._robot = Robot()

    def get_robot(self):
        return self._robot

    def build_robot_head(self):
        self._robot.set_robot_head("Tin Head")

    def build_robot_legs(self):
        self._robot.set_robot_legs("Tin legs")

    def build_robot_torso(self):
        self._robot.set_robot_torso("Tin torso")

    def build_robot_arms(self):
        self._robot.set_robot_arms("Tin arms")


class RobotEngineer:
    def __init__(self, robot_builder) -> None:
        self._robot_builder = robot_builder

    def get_robot(self):
        return self._robot_builder.get_robot()

    def make_robot(self):
        self._robot_builder.build_robot_arms()
        self._robot_builder.build_robot_legs()
        self._robot_builder.build_robot_head()
        self._robot_builder.build_robot_torso()


ceto = OldRobotBuilder()
ranachowski = RobotEngineer(ceto)
ranachowski.make_robot()
first = ranachowski.get_robot()
print(first)
