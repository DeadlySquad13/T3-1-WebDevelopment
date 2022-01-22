package com.ds13.anitracker;

import androidx.annotation.NonNull;
import androidx.annotation.RequiresApi;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Build;
import android.os.Bundle;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;

import com.bumptech.glide.Glide;

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
                            fillAnimeDetails(anime);
                        }
                    }

                    @Override
                    public void onFailure(@NonNull Call<Anime> call, @NonNull Throwable t) {
                        t.printStackTrace();
                    }
                });
    }

    // Parse object and fill view with data.
    protected void fillAnimeDetails(Anime anime) {
        // Title.
        TextView title = findViewById(R.id.title);
        title.setText(anime.getTitle());

        // Poster.
        ImageView imageView = (ImageView) findViewById(R.id.poster);
        Glide.with(this).load(anime.getPoster()).into(imageView);

        // Description.
        TextView description = findViewById(R.id.description);
        description.setText(anime.getDescription());
    }

    // Go back to the MainActivity.
    public void goBack(View view) {
        Intent intent = new Intent(this, MainActivity.class);
        startActivity(intent);
    }
}