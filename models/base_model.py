
class BaseModel:
    def to_dict(self, excluded_fields=['DOB', 'updated_at', '_sa_instance_state']):

        student = self.__dict__.copy()
        excluded_set = set(excluded_fields)

        needed = {key:value for key, value in student.items() if key not in excluded_set}

        return needed
