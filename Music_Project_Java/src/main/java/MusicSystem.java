import com.wrapper.spotify.SpotifyApi;
import com.wrapper.spotify.model_objects.credentials.ClientCredentials;
import com.wrapper.spotify.requests.authorization.client_credentials.ClientCredentialsRequest;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.concurrent.CancellationException;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.CompletionException;


/*
This code will not do much, since Spotify does not have any 
 */

public class MusicSystem{

    // Don't know which constructors we would prefer at this point
    public MusicSystem(){

    }
    public Track[] getTracks(){
        return new Track[10];
    }

//    public Track[] sortTracks(Track[] tracks, int attr){
//        switch(attr){
//            case 8:{
//                for()
//            }
//        }
//    }

    public static void spotifyTest(){
        String clientId = "3a5dd16e5d8c4367bc50f10853081107";
        String clientSecret = "6174229408c24f3ea6696663273b2b97";
//        URI redirectUri = SpotifyHttpManager.makeUri("https://app.getpostman.com/oauth2/callback");
        SpotifyApi spotifyApi = new SpotifyApi.Builder().setClientId(clientId).setClientSecret(clientSecret).build();
        ClientCredentialsRequest clientCredentialsRequest = spotifyApi.clientCredentials().build();
        try {
            final CompletableFuture<ClientCredentials> clientCredentialsFuture = clientCredentialsRequest.executeAsync();

            // Thread free to do other tasks...

            // Example Only. Never block in production code.
            final ClientCredentials clientCredentials = clientCredentialsFuture.join();

            // Set access token for further "spotifyApi" object usage
            spotifyApi.setAccessToken(clientCredentials.getAccessToken());

            System.out.println("Expires in: " + clientCredentials.getExpiresIn());
        } catch (CompletionException e) {
            System.out.println("Error: " + e.getCause().getMessage());
        } catch (CancellationException e) {
            System.out.println("Async operation cancelled.");
        }
    }
    public void generatePlaylistMood(int mood){
        Track[] tList = getTracks();
        ArrayList<Track> tracks = new ArrayList<Track>();
        switch(mood){
            case 1: {
                // Happy
//                Arrays.stream();
            }
            case 2: {
                // Happy
            }
            case 3: {
                // Happy
            }
            case 4: {
                // Happy
            }
        }
    }

    public static void main(String [] args){
        spotifyTest();
    }
}
