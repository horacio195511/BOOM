# input: cartID, this system would dispatch order with the same cartID to different maker, or the same user based on
# the geo location and quality.
from Market.models import Order


class Dispatcher:
    def unpack(self, cartID):
        orderList = Order.objects.get(cartID=cartID)
        return orderList

    def dispatch_to_printer(self, orderList):

    # get all of the printer in the area
    # calculate their distance with user
    # use filter to find those in 5->10->15->20 mile
    # dispatch to
    # aggregate them by user
    # sent order message to user

    def dispatch_to_user(self, orderList):
# dispatch order to user based on their userID
