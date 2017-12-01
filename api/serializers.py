from rest_framework import serializers
from .models import Company, Listing

# serializers


class CompanySerializer(serializers.ModelSerializer):
    listings = serializers.StringRelatedField(many=True)
    user = serializers.StringRelatedField(many=False)

    class Meta:
        model = Company
        fields = ("name", "user", "short_description",
                  "official_website", "listings")


class ListingSerializer(serializers.ModelSerializer):
    company = serializers.StringRelatedField(many=False)

    class Meta:
        model = Listing
        fields = ("title", "location", "company",
                  "job_description", "application_link",
                  "date_created")
