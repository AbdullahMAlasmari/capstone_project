AUTH0_DOMAIN_settingup = 'dev-jddprej2.us.auth0.com'
ALGORITHMS_settingup = ['RS256']
API_AUDIENCE_settingup = 'movieapi'
CLIENT_ID = 'h396b6UoLNVKKiXlX0Ru1neP7waXnm6S'

host_url = "http://0.0.0.0:8080/"

executive_producer_headers = {
    "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkZ4dHhUY21EdGdPNUxVeEVmQ1F2cCJ9.eyJpc3MiOiJodHRwczovL2Rldi1qZGRwcmVqMi51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYzN2M3ZDA0NzY2ODMwMDY3ZWE4M2FhIiwiYXVkIjoibW92aWVhcGkiLCJpYXQiOjE1OTg2MTgwNDgsImV4cCI6MTU5ODcwNDQ0OCwiYXpwIjoiaDM5NmI2VW9MTlZLS2lYbFgwUnUxbmVQN3dhWG5tNlMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.eb8Vrhm9_aWKk4VpFZpl-RREHRMWYGeP6QFIux2CpPALxnJFmFo1LOcYO0JngCKKjvrVFtSMeQsU0MRbN4jpAHckhIKtX-SQVhMZvlJweHqmHBUvdk0ytLKeovDT5pfeAHDkIQOJKNPsckU-OB9N0xQDXTNP6YGAPfosuWETgephTnDsjgUuXWIA5tH5tDz1Atgf_KTjyVEEaUyjEC_Mt7iY03PvrB84g1T0V0kp3TChWHl8Nk8pvnw2YxHA8he3FJKXpQZFMgMW285D832xAgWVh8OwrSIeWeNUFBw9B4SBHO4WLknEA28voJ9gPwhPBXm98ixQr1eqmrjJ-SA_wQ",
    "Content-Type": "application/json"
}

casting_assistant_headers = {
    "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkZ4dHhUY21EdGdPNUxVeEVmQ1F2cCJ9.eyJpc3MiOiJodHRwczovL2Rldi1qZGRwcmVqMi51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYzODIwY2EzOGQxYTIwMDZkMjEzNWZhIiwiYXVkIjoibW92aWVhcGkiLCJpYXQiOjE1OTg2MTgwOTUsImV4cCI6MTU5ODcwNDQ5NSwiYXpwIjoiaDM5NmI2VW9MTlZLS2lYbFgwUnUxbmVQN3dhWG5tNlMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIl19.FN3eaQNWr7-gjbBmvt9mrZ3BGy8LGuOm6beEAQM2PA54PIkeQcbfHZSW8NgJW65E-7-d1H3Toavy4iBa2U4ccd1krRqoCz8-rZ4oFnKciT8IL5Wneq_mMG9MLtCWJ-9mbsdfe2hDiay8VuRMUfJGFkZiIUyicUPobfaydojy_ODajU41qtzDUwCevOSCkrAiLxiuS3zpJurVNwyfaUd8EUIad1J5fsuiwZJXAb54sUdLsb7i-F7H3gGucGvfDzeV3bM79vfXCV6tp5oClzaVWES43uKV3E5LNwMHAwAyXq3IOOxt5X1aVa-IFIVLIMTXq1oxtjdnoZqzjaziJ6Zg5Q",
    "Content-Type": "application/json"
}

casting_director_headers = {
    "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkZ4dHhUY21EdGdPNUxVeEVmQ1F2cCJ9.eyJpc3MiOiJodHRwczovL2Rldi1qZGRwcmVqMi51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYzODIyMGFmZTQ1MjcwMDZkOTMyMmU4IiwiYXVkIjoibW92aWVhcGkiLCJpYXQiOjE1OTg2MTgxMzUsImV4cCI6MTU5ODcwNDUzNSwiYXpwIjoiaDM5NmI2VW9MTlZLS2lYbFgwUnUxbmVQN3dhWG5tNlMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIl19.H7gbQtrPwaZ_p5GfTfEhapnLGeoStY915-TjN7bzK0HugRNnxqn5F4cplqbrnXCotGbPEiAcABNTactx8mxKc9ZWFwV0s7oFpOJwUC-NmISVRGpzZNiaJbBhm9tzV2UGhV8h_H_5p9zXlhaAuf2O8Z2pE5s0rZmpqvAa3XhoxAk54z-MxHFvm_t6UT64N-ROjRqmtzROPZZvFJkSbFfZ12ov3O8MRK8wAOCvBW1r9myfangpkyNGlITFHKfxBGoc4uWTPlzc3E13t7VQlQcDEBu7q66AeO7hzeksGW0YRGzARN_TIdjH_0R644mfLIO5ZusghOxcwkEW13Rad8t6Ig",
    "Content-Type": "application/json"
}