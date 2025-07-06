class Show:
    def __init__(self,sh_id,sh_time,scr_num,seats):
        self.sh_id=sh_id
        self.sh_time=sh_time
        self.scr_num=scr_num
        self.seats=seats

    def get_available_seats(self):
        available=[]
        for seat in self.seats:

            if seat.get_status()=="Available":
                available.append(seat)
        return available


    def reserve_seats(self,seat_ids):
        c=0
        for seat in self.seats:

            if seat.s_id in seat_ids:
                if seat.reserve_seat():
                    c+=1
        if c==len(seat_ids):
            return True
        else:
            return False

    def unreserve_seats(self, seat_ids):
        c = 0
        for seat in self.seats:

            if seat.s_id in seat_ids:
                if seat.unreserve_seat():
                    c += 1
        if c == len(seat_ids):
            return True
        else:
            return False


    def get_details(self):
        return self.sh_id,self.sh_time,self.scr_num