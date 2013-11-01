from plone.autoform.interfaces import IFormFieldProvider
from plone.directives import form
from plone.supermodel import model
from zope.interface import alsoProvides
from z3c.relationfield.schema import RelationList, RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder

from zope.i18nmessageid import MessageFactory
CollectiveCarouselMessageFactory = MessageFactory('collective.carousel')


class ICollectiveCarouselBehaviour(model.Schema):
    """
       Marker/Form interface for Collective Carousel Behaviour
    """

    form.fieldset(
        'carousel',
        label=CollectiveCarouselMessageFactory(
            'fieldset_carousel', default=u'Carousel'),
        fields=(
            'carouselprovider',
        ),
    )

    carouselprovider = RelationList(
        title=CollectiveCarouselMessageFactory(
            u"label_carouselprovider_title", default=u"Carousel object."),
        description=CollectiveCarouselMessageFactory(
            u"help_carouselprovider",
            default=u"Object providing items (content) for carousel."),
        default=[],
        value_type=RelationChoice(source=ObjPathSourceBinder(
            portal_type=('Topic', 'Collection',)),),
        required=False,
        )


alsoProvides(ICollectiveCarouselBehaviour, IFormFieldProvider)


def context_property(name):

    def getter(self):
        return getattr(self.context, name)

    def setter(self, value):
        setattr(self.context, name, value)

    def deleter(self):
        delattr(self.context, name)
    return property(getter, setter, deleter)
