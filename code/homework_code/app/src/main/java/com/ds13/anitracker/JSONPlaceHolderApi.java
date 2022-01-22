package com.ds13.anitracker;

import java.util.List;

import retrofit2.Call;
import retrofit2.http.GET;
import retrofit2.http.Path;

public interface JSONPlaceHolderApi {
    @GET("/anime")
    public Call<List<Anime>> getAllAnime();

    @GET("/anime/{pk}")
    public Call<Anime> getAnimeDetails(@Path("pk") int animeId);
}
