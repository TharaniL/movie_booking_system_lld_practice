class Seat:

    def __init__(self,s_id,s_name,s_type,s_status,s_rate):
        self.s_id=s_id
        self.s_name=s_name
        self.s_type=s_type
        self._s_status=s_status
        self.s_rate=s_rate

    def reserve_seat(self):

        if self._s_status=="Available":
            self._s_status="Reserved"
            return True
        return False

    def unreserve_seat(self):

        if self._s_status=="Reserved":
            self._s_status="Available"
            return True
        return False


    def get_status(self):
        return self._s_status
