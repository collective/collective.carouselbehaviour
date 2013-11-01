from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.supermodel import model
from zope import schema
from zope.component import adapts
from zope.interface import alsoProvides, implements

from collective.carouselbehaviour import MessageFactory as _


class ICollectiveCarouselBehaviour(model.Schema):
    """
       Marker/Form interface for Collective Carousel Behaviour
    """

    # -*- Your Zope schema definitions here ... -*-


alsoProvides(ICollectiveCarouselBehaviour, IFormFieldProvider)

def context_property(name):
    def getter(self):
        return getattr(self.context, name)
    def setter(self, value):
        setattr(self.context, name, value)
    def deleter(self):
        delattr(self.context, name)
    return property(getter, setter, deleter)


class CollectiveCarouselBehaviour(object):
    """
       Adapter for Collective Carousel Behaviour
    """
    implements(ICollectiveCarouselBehaviour)
    adapts(IDexterityContent)

    def __init__(self,context):
        self.context = context

    # -*- Your behavior property setters & getters here ... -*-
