from __future__ import unicode_literals

from django.conf.urls import patterns, url

from .views import (
    AllDocumentSignatureVerifyView, DocumentVersionSignatureDeleteView,
    DocumentVersionSignatureDetailView, DocumentVersionSignatureDownloadView,
    DocumentVersionSignatureListView, DocumentVersionSignatureUploadView
)

urlpatterns = patterns(
    '',
    url(
        r'^(?P<pk>\d+)/details/$',
        DocumentVersionSignatureDetailView.as_view(),
        name='document_version_signature_details'
    ),
    url(
        r'^signature/(?P<pk>\d+)/download/$',
        DocumentVersionSignatureDownloadView.as_view(),
        name='document_version_signature_download'
    ),
    url(
        r'^document/version/(?P<pk>\d+)/signatures/list/$',
        DocumentVersionSignatureListView.as_view(),
        name='document_version_signature_list'
    ),
    url(
        r'^documents/version/(?P<pk>\d+)/signature/upload/$',
        DocumentVersionSignatureUploadView.as_view(),
        name='document_version_signature_upload'
    ),
    url(
        r'^signature/(?P<pk>\d+)/delete/$',
        DocumentVersionSignatureDeleteView.as_view(),
        name='document_version_signature_delete'
    ),
    url(
        r'^tools/all/document/version/signature/verify/$',
        AllDocumentSignatureVerifyView.as_view(),
        name='all_document_version_signature_verify'
    ),
)
