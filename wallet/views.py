from rest_framework import generics, status
from rest_framework.response import Response
from .models import Wallet
from .serializers import WalletSerializer


class WalletListAPIView(generics.ListAPIView, generics.DestroyAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer

    def deletel(request, pk):
        print("masuk rsa")
        try:
            instance = Wallet.objects.get(pk=pk)
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Wallet.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

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


class WalletDetail(generics.RetrieveUpdateDestroyAPIView):
    def patch(self, request, pk):
        try:
            instance = Wallet.objects.get(id=pk)
        except Wallet.DoesNotExist:
            return Response(
                {"error": "Object does not exist"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = WalletSerializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
