Introduction
============

This package provides the ability to assign carousel information to
Dexterity-based (``plone.app.dexterity``) content types within `Plone`_ and 
does so using `collective.carousel`_.

By applying the behaviour from this package to a Dexterity content type, a
`Carousel` field becomes available when creating or editing said content.

Found a bug? Please, use the `issue tracker`_.

.. contents:: Table of contents


Installation
============

This addon can be installed has any other addons, please follow official
documentation_.

Usage
-----

Through the web
^^^^^^^^^^^^^^^^

If you are configuring your Dexterity-based type through the web-based
interface, then proceed to edit your content type in the `Dexterity Content
Types` control panel. Under the `Behaviours` tab you will find the
``Collective Carousel Behaviour`` behaviour -- select this and save your 
content type.

Upon adding or editing an object of your content type, you will see the new
field accordingly.

Generic Setup (file system)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you've created a file-system Dexterity type configuration, you need to
specify the relevant interface as a behaviour::

    collective.carouselbehaviour.collectivecarouselbehaviour.ICollectiveCarouselBehaviour

and import or re-import your type configuration.  As an example, a type
configuration at ``${product_dir}/profiles/default/types/my.datatype.xml``
would look like this::

    <?xml version="1.0"?>
    <object name="my.datatype"
        meta_type="Dexterity FTI"
        xmlns:i18n="http://xml.zope.org/namespaces/i18n"
        i18n:domain="tdh.metadata">
        ...
        <property name="behaviors">
            <element value="collective.carouselbehaviour.collectivecarouselbehaviour.ICollectiveCarouselBehaviour"/>
        </property>
        ...
    </object>

.. _documentation: http://developer.plone.org/getstarted/installing_addons.html
.. _issue tracker: https://github.com/collective/collective.carouselbehaviour
.. _Plone: http://plone.org
.. _collective.carousel: http://pypi.python.org/pypi/collective.carousel
.. _WKT: http://en.wikipedia.org/wiki/Well-known_text
