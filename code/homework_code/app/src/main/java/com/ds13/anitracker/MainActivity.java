package com.ds13.anitracker;

import androidx.annotation.NonNull;
import androidx.annotation.RequiresApi;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Build;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.ListView;

import java.util.List;
import java.util.stream.Collectors;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class MainActivity extends AppCompatActivity {
    @RequiresApi(api = Build.VERSION_CODES.N)
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        this.fetchAnime();
    }

    protected void fillListWithStrings(ListView list, List<String> strings) {
        // Create adapter.
        ArrayAdapter<String> adapter = new ArrayAdapter<>(this, android.R.layout.simple_list_item_1, strings);

        // Assign adapter to ListView.
        list.setAdapter(adapter);
    }

    protected void fetchAnime() {
        NetworkService.getInstance()
                .getJSONApi()
                .getAllAnime()
                .enqueue(new Callback<List<Anime>>() {
                    @RequiresApi(api = Build.VERSION_CODES.N)
                    @Override
                    public void onResponse(@NonNull Call<List<Anime>> call, @NonNull Response<List<Anime>> response) {
                        List<Anime> animeInstances = response.body();

                        if (animeInstances != null) {
                            // Map animeInstances to list of string containing anime titles.
                            List<String> animeTitles = animeInstances.stream().map(Anime::getTitle).collect(Collectors.toList());

                            // Get ListView and fill it with items.
                            ListView animeList = findViewById(R.id.animeList);

                            fillListWithStrings(animeList, animeTitles);

                            // List item click handler.
                            animeList.setOnItemClickListener(new AdapterView.OnItemClickListener() {
                                @Override
                                public void onItemClick(AdapterView<?> adapterView, View view, int i, long id) {
                                    // By selecting an element by position of the list item that was clicked.

                                    Anime selectedItem = animeInstances.get(i);
                                    showAnimeDetails(selectedItem.getPk());
                                }
                            });
                        }
                    }

                    @Override
                    public void onFailure(@NonNull Call<List<Anime>> call, @NonNull Throwable t) {
                        t.printStackTrace();
                    }
                });
    }


    protected void showAnimeDetails(int animePk) {
        Intent intent = new Intent(this, AnimeDetailsActivity.class);
        intent.putExtra("animePk", animePk);
        startActivity(intent);
    }
}
