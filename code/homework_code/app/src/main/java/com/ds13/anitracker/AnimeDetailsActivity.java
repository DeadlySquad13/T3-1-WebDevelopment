package com.ds13.anitracker;

import androidx.annotation.NonNull;
import androidx.annotation.RequiresApi;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Build;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ListView;

import java.util.List;
import java.util.stream.Collectors;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class AnimeDetailsActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_anime_details);
        Bundle arguments = getIntent().getExtras();
        int animePk = arguments.getInt("animePk");
        this.fetchAnime(animePk);
    }

    public void goBack(View view) {
        Intent intent = new Intent(this, MainActivity.class);
        startActivity(intent);
    }

    protected void fetchAnime(int pk) {
        NetworkService.getInstance()
                .getJSONApi()
                .getAnimeDetails(pk)
                .enqueue(new Callback<Anime>() {
                    @RequiresApi(api = Build.VERSION_CODES.N)
                    @Override
                    public void onResponse(@NonNull Call<Anime> call, @NonNull Response<Anime> response) {
                        Anime anime = response.body();

                        if (anime != null) {
                            // Get ListView and fill it with items.
                        }
                    }

                    @Override
                    public void onFailure(@NonNull Call<Anime> call, @NonNull Throwable t) {
                        t.printStackTrace();
                    }
                });
    }
}