from collective.carousel.browser.viewlets import CarouselViewlet as CarouselViewletInitial


class CarouselViewlet(CarouselViewletInitial):
    def getProviders(self):
        schema = getattr(self.context, 'carouselprovider', None)
        if schema is None:
            return None
        return [i.to_object for i in self.context.carouselprovider]
