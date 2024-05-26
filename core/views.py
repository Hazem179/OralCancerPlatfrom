from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .utils import CustomPagination
from .models import *
from .serializers import DoctorSerializer,SpecializationSerializer,CertificationSerializer,TagSerializer,PostSerializer,PostTagsSerializer,CommentSerializer,ContactSerializer, VideoBlogSerializer



@swagger_auto_schema(
    method='get',
    operation_description="Retrieve the list of doctors.",
    responses={
        200: openapi.Response('OK', DoctorSerializer(many=True)),
    }
)
@swagger_auto_schema(
    method='post',
    operation_description="Create a new doctor.",
    request_body=DoctorSerializer,
    responses={
        201: openapi.Response('Created', DoctorSerializer),
        400: openapi.Response('Bad Request', None),
    }
)
@api_view(['GET', 'POST'])
def doctor_list_create(request):
    pagination = CustomPagination()
    if request.method == 'GET':
        doctors = Doctor.objects.all()
        paginated_doctors = pagination.paginate_queryset(doctors, request)
        serializer = DoctorSerializer(paginated_doctors, many=True)
        return pagination.get_paginated_response(serializer.data)
    elif request.method == 'POST':
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method='get',
    operation_description="Retrieve a doctor by ID.",
    responses={
        200: openapi.Response('OK', DoctorSerializer),
        404: openapi.Response('Not Found', None),
    }
)
@swagger_auto_schema(
    method='put',
    operation_description="Update a doctor by ID.",
    request_body=DoctorSerializer,
    responses={
        200: openapi.Response('OK', DoctorSerializer),
        400: openapi.Response('Bad Request', None),
        404: openapi.Response('Not Found', None),
    }
)
@swagger_auto_schema(
    method='delete',
    operation_description="Delete a doctor by ID.",
    responses={
        204: openapi.Response('No Content', None),
        404: openapi.Response('Not Found', None),
    }
)
@api_view(['GET', 'PUT', 'DELETE'])
def doctor_detail(request, pk):
    try:
        doctor = Doctor.objects.get(pk=pk)
    except Doctor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = DoctorSerializer(doctor)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = DoctorSerializer(doctor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        doctor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@swagger_auto_schema(
    method='get',
    operation_description="Retrieve the list of specializations.",
    responses={
        200: openapi.Response('OK', SpecializationSerializer(many=True)),
    }
)
@swagger_auto_schema(
    method='post',
    operation_description="Create a new specialization.",
    request_body=SpecializationSerializer,
    responses={
        201: openapi.Response('Created', SpecializationSerializer),
        400: openapi.Response('Bad Request', None),
    }
)
@api_view(['GET', 'POST'])
def specialization_list_create(request):
    if request.method == 'GET':
        specializations = Specialization.objects.all()
        serializer = SpecializationSerializer(specializations, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SpecializationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(
    method='get',
    operation_description="Retrieve a specialization by ID.",
    responses={
        200: openapi.Response('OK', SpecializationSerializer),
        404: openapi.Response('Not Found', None),
    }
)
@swagger_auto_schema(
    method='put',
    operation_description="Update a specialization by ID.",
    request_body=SpecializationSerializer,
    responses={
        200: openapi.Response('OK', SpecializationSerializer),
        400: openapi.Response('Bad Request', None),
        404: openapi.Response('Not Found', None),
    }
)
@swagger_auto_schema(
    method='delete',
    operation_description="Delete a specialization by ID.",
    responses={
        204: openapi.Response('No Content', None),
        404: openapi.Response('Not Found', None),
    }
)
@api_view(['GET', 'PUT', 'DELETE'])
def specialization_detail(request, pk):
    try:
        specialization = Specialization.objects.get(pk=pk)
    except Specialization.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SpecializationSerializer(specialization)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SpecializationSerializer(specialization, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        specialization.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@swagger_auto_schema(
    method='get',
    operation_description="Retrieve the list of specializations.",
    responses={
        200: openapi.Response('OK', SpecializationSerializer(many=True)),
    }
)
@swagger_auto_schema(
    method='post',
    operation_description="Create a new specialization.",
    request_body=SpecializationSerializer,
    responses={
        201: openapi.Response('Created', SpecializationSerializer),
        400: openapi.Response('Bad Request', None),
    }
)
@api_view(['GET', 'POST'])
def certification_list_create(request):
    if request.method == 'GET':
        certifications = Certification.objects.all()
        serializer = CertificationSerializer(certifications, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CertificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(
    method='get',
    operation_description="Retrieve a certification by ID.",
    responses={
        200: openapi.Response('OK', CertificationSerializer),
        404: openapi.Response('Not Found', None),
    }
)
@swagger_auto_schema(
    method='put',
    operation_description="Update a certification by ID.",
    request_body=CertificationSerializer,
    responses={
        200: openapi.Response('OK', CertificationSerializer),
        400: openapi.Response('Bad Request', None),
        404: openapi.Response('Not Found', None),
    }
)
@swagger_auto_schema(
    method='delete',
    operation_description="Delete a certification by ID.",
    responses={
        204: openapi.Response('No Content', None),
        404: openapi.Response('Not Found', None),
    }
)
@api_view(['GET', 'PUT', 'DELETE'])
def certification_detail(request, pk):
    try:
        certification = Certification.objects.get(pk=pk)
    except Certification.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CertificationSerializer(certification)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CertificationSerializer(certification, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        certification.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@swagger_auto_schema(
    method='get',
    operation_description="Retrieve the list of tags.",
    responses={
        200: openapi.Response('OK', TagSerializer(many=True)),
    }
)
@swagger_auto_schema(
    method='post',
    operation_description="Create a new tag.",
    request_body=TagSerializer,
    responses={
        201: openapi.Response('Created', TagSerializer),
        400: openapi.Response('Bad Request', None),
    }
)
@api_view(['GET', 'POST'])
def tag_list_create(request):
    pagination = CustomPagination()
    if request.method == 'GET':
        tags = Tag.objects.all()
        paginated_tags = pagination.paginate_queryset(tags, request)
        serializer = TagSerializer(paginated_tags, many=True)
        return pagination.get_paginated_response(serializer.data)

    elif request.method == 'POST':
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(
    method='get',
    operation_description="Retrieve a tag by ID.",
    responses={
        200: openapi.Response('OK', TagSerializer),
        404: openapi.Response('Not Found', None),
    }
)
@swagger_auto_schema(
    method='put',
    operation_description="Update a tag by ID.",
    request_body=TagSerializer,
    responses={
        200: openapi.Response('OK', TagSerializer),
        400: openapi.Response('Bad Request', None),
        404: openapi.Response('Not Found', None),
    }
)
@swagger_auto_schema(
    method='delete',
    operation_description="Delete a tag by ID.",
    responses={
        204: openapi.Response('No Content', None),
        404: openapi.Response('Not Found', None),
    }
)
@api_view(['GET', 'PUT', 'DELETE'])
def tag_detail(request, pk):
    try:
        tag = Tag.objects.get(pk=pk)
    except Tag.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TagSerializer(tag)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TagSerializer(tag, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        tag.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
###########################################################

@swagger_auto_schema(
    method='get',
    operation_description="Retrieve the list of posts.",
    responses={
        200: openapi.Response('OK', PostSerializer(many=True)),
    }
)
@swagger_auto_schema(
    method='post',
    operation_description="Create a new post.",
    request_body=PostSerializer,
    responses={
        201: openapi.Response('Created', PostSerializer),
        400: openapi.Response('Bad Request', None),
    }
)
@api_view(['GET', 'POST'])
def post_list_create(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(
    method='get',
    operation_description="Retrieve a post by ID.",
    responses={
        200: openapi.Response('OK', PostSerializer),
        404: openapi.Response('Not Found', None),
    }
)
@swagger_auto_schema(
    method='put',
    operation_description="Update a post by ID.",
    request_body=PostSerializer,
    responses={
        200: openapi.Response('OK', PostSerializer),
        400: openapi.Response('Bad Request', None),
        404: openapi.Response('Not Found', None),
    }
)
@swagger_auto_schema(
    method='delete',
    operation_description="Delete a post by ID.",
    responses={
        204: openapi.Response('No Content', None),
        404: openapi.Response('Not Found', None),
    }
)
@api_view(['GET', 'PUT', 'DELETE'])
def post_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@swagger_auto_schema(
    method='get',
    operation_description="Retrieve the list of post tags.",
    responses={
        200: openapi.Response('OK', PostTagsSerializer(many=True)),
    }
)
@swagger_auto_schema(
    method='post',
    operation_description="Create a new post tag.",
    request_body=PostTagsSerializer,
    responses={
        201: openapi.Response('Created', PostTagsSerializer),
        400: openapi.Response('Bad Request', None),
    }
)
@api_view(['GET', 'POST'])
def post_tags_list_create(request):
    if request.method == 'GET':
        post_tags = PostTags.objects.all()
        serializer = PostTagsSerializer(post_tags, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PostTagsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(
    method='get',
    operation_description="Retrieve a post tag by ID.",
    responses={
        200: openapi.Response('OK', PostTagsSerializer),
        404: openapi.Response('Not Found', None),
    }
)
@swagger_auto_schema(
    method='put',
    operation_description="Update a post tag by ID.",
    request_body=PostTagsSerializer,
    responses={
        200: openapi.Response('OK', PostTagsSerializer),
        400: openapi.Response('Bad Request', None),
        404: openapi.Response('Not Found', None),
    }
)
@swagger_auto_schema(
    method='delete',
    operation_description="Delete a post tag by ID.",
    responses={
        204: openapi.Response('No Content', None),
        404: openapi.Response('Not Found', None),
    }
)
@api_view(['GET', 'PUT', 'DELETE'])
def post_tags_detail(request, pk):
    try:
        post_tags = PostTags.objects.get(pk=pk)
    except PostTags.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PostTagsSerializer(post_tags)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PostTagsSerializer(post_tags, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        post_tags.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@swagger_auto_schema(
    method='get',
    operation_description="Retrieve the list of comments.",
    responses={
        200: openapi.Response('OK', CommentSerializer(many=True)),
    }
)
@swagger_auto_schema(
    method='post',
    operation_description="Create a new comment.",
    request_body=CommentSerializer,
    responses={
        201: openapi.Response('Created', CommentSerializer),
        400: openapi.Response('Bad Request', None),
    }
)
@api_view(['GET', 'POST'])
def comment_list_create(request):
    if request.method == 'GET':
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(
    method='get',
    operation_description="Retrieve a comment by ID.",
    responses={
        200: openapi.Response('OK', CommentSerializer),
        404: openapi.Response('Not Found', None),
    }
)
@swagger_auto_schema(
    method='put',
    operation_description="Update a comment by ID.",
    request_body=CommentSerializer,
    responses={
        200: openapi.Response('OK', CommentSerializer),
        400: openapi.Response('Bad Request', None),
        404: openapi.Response('Not Found', None),
    }
)
@swagger_auto_schema(
    method='delete',
    operation_description="Delete a comment by ID.",
    responses={
        204: openapi.Response('No Content', None),
        404: openapi.Response('Not Found', None),
    }
)
@api_view(['GET', 'PUT', 'DELETE'])
def comment_detail(request, pk):
    try:
        comment = Comment.objects.get(pk=pk)
    except Comment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@swagger_auto_schema(
    method='get',
    operation_description="Retrieve the list of videoblogs.",
    responses={
        200: openapi.Response('OK', VideoBlogSerializer(many=True)),
    }
)
@swagger_auto_schema(
    method='post',
    operation_description="Create a new videoblog.",
    request_body=VideoBlogSerializer,
    responses={
        201: openapi.Response('Created', VideoBlogSerializer),
        400: openapi.Response('Bad Request', None),
    }
)
@api_view(['GET', 'POST'])
def videoblog_list_create(request):
    if request.method == 'GET':
        videoblogs = VideoBlog.objects.all()
        serializer = VideoBlogSerializer(videoblogs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = VideoBlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(
    method='get',
    operation_description="Retrieve a videoblog by ID.",
    responses={
        200: openapi.Response('OK', VideoBlogSerializer),
        404: openapi.Response('Not Found', None),
    }
)
@swagger_auto_schema(
    method='put',
    operation_description="Update a videoblog by ID.",
    request_body=VideoBlogSerializer,
    responses={
        200: openapi.Response('OK', VideoBlogSerializer),
        400: openapi.Response('Bad Request', None),
        404: openapi.Response('Not Found', None),
    }
)
@swagger_auto_schema(
    method='delete',
    operation_description="Delete a videoblog by ID.",
    responses={
        204: openapi.Response('No Content', None),
        404: openapi.Response('Not Found', None),
    }
)
@api_view(['GET', 'PUT', 'DELETE'])
def videoblog_detail(request, pk):
    try:
        videoblog = VideoBlog.objects.get(pk=pk)
    except VideoBlog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = VideoBlogSerializer(videoblog)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = VideoBlogSerializer(videoblog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        videoblog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@swagger_auto_schema(
    method='get',
    operation_description="Retrieve the list of contacts.",
    responses={
        200: openapi.Response('OK', ContactSerializer(many=True)),
    }
)
@swagger_auto_schema(
    method='post',
    operation_description="Create a new contact.",
    request_body=ContactSerializer,
    responses={
        201: openapi.Response('Created', ContactSerializer),
        400: openapi.Response('Bad Request', None),
    }
)
@api_view(['GET', 'POST'])
def contact_list_create(request):
    if request.method == 'GET':
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(
    method='get',
    operation_description="Retrieve a contact by ID.",
    responses={
        200: openapi.Response('OK', ContactSerializer),
        404: openapi.Response('Not Found', None),
    }
)
@swagger_auto_schema(
    method='put',
    operation_description="Update a contact by ID.",
    request_body=ContactSerializer,
    responses={
        200: openapi.Response('OK', ContactSerializer),
        400: openapi.Response('Bad Request', None),
        404: openapi.Response('Not Found', None),
    }
)
@swagger_auto_schema(
    method='delete',
    operation_description="Delete a contact by ID.",
    responses={
        204: openapi.Response('No Content', None),
        404: openapi.Response('Not Found', None),
    }
)
@api_view(['GET', 'PUT', 'DELETE'])
def contact_detail(request, pk):
    try:
        contact = Contact.objects.get(pk=pk)
    except Contact.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ContactSerializer(contact)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ContactSerializer(contact, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        contact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)