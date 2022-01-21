package com.ds13.anitracker;

import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class NetworkService {
    private static NetworkService instance;
    private static final String BASE_URL = "http://10.0.2.2:8000";
    private Retrofit retrofit;

    private NetworkService() {
        this.retrofit = new Retrofit.Builder()
                .baseUrl(BASE_URL)
                .addConverterFactory(GsonConverterFactory.create())
                .build();
    }

    public static NetworkService getInstance() {
        if (instance == null) {
            instance = new NetworkService();
        }

        return instance;
    }

    public JSONPlaceHolderApi getJSONApi() {
        return this.retrofit.create(JSONPlaceHolderApi.class);
    }
}
