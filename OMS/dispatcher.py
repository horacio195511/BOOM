# input: cartID, this system would dispatch order with the same cartID to different maker, or the same user based on
# the geo location and quality.
from Market.models import Order
from Market.models import Cart


class Dispatcher:
    def unpack(self, userID):
        orderList = Cart.objects.get(user=userID)
        return orderList

    def find_printer(self, userID):
        '''
        :param userID: one user only have one cart, so I directly use userID
        :return: multiple order object
        '''
        # get all of the order from cart
        orderList = self.unpack(userID)
        # find printer for all of the order, seperate them if neccessary
        for order in orderList:
            # TODO: dispatch utility not completed yet
            orderList.printer = "hello"
        return orderList
