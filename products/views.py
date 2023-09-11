from rest_framework import generics, status
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer


class ProductListAPIView(generics.ListAPIView):
    # permission_classes = [IsAuthenticated, ]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def post(self, request):
        try:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        "status": 201,
                        "message": "POST successful",
                        "data": serializer.data,
                    },
                    status=status.HTTP_201_CREATED,
                )
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except TypeError:
            return Response(
                {"message": "Ada input yang tidak masuk."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except Exception as e:
            return Response(
                {"message": "Ada yang salah proses POST data."},
                status=status.HTTP_400_BAD_REQUEST,
            )


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    def patch(self, request, pk):
        try:
            instance = Product.objects.get(id=pk)
        except Product.DoesNotExist:
            return Response(
                {"error": "Object does not exist"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = ProductSerializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
