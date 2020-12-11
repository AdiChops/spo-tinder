import java.util.Date;

public class Track {
    private String trackName;
    private Artist artist;
    private Album album;
    private Date releaseDate;
    private double length;
    private int popularity;
    private double danceability;
    private double acousticness;
    private double energy;
    private double instrumentalness;
    private double liveness;
    private double loudness;
    private double speechiness;
    private double tempo;
    private int timeSignature;
    private boolean isBlacklisted;
    private String spotifyUri;


    // JUST TEMPORARY FOR TESTING
    public Track(String name){
        this.trackName = name;
    }

    public Track(String trackName, Artist artist, Album album, Date releaseDate, double length, int popularity, double danceability, double acousticness, double energy, double instrumentalness, double liveness, double loudness, double speechiness, double tempo, int timeSignature, boolean isBlacklisted, String spotifyUri){
        this.trackName = trackName;
        this.artist = artist;
        this.album = album;
        this.releaseDate = releaseDate;
        this.length = length;
        this.popularity = popularity;
        this.danceability = danceability;
        this.acousticness = acousticness;
        this.energy = energy;
        this.instrumentalness = instrumentalness;
        this.liveness = liveness;
        this.loudness = loudness;
        this.speechiness = speechiness;
        this.tempo = tempo;
        this.timeSignature = timeSignature;
        this.isBlacklisted = false;
        this.spotifyUri = spotifyUri;
    }


    public String getTrackName() {return trackName;}
    public void setTrackName(String trackName) {this.trackName = trackName;}

    public Artist getArtist() {return artist; }
    public void setArtist(Artist artist) { this.artist = artist; }

    public Album getAlbum() {  return album; }
    public void setAlbum(Album album) {this.album = album; }

    public Date getReleaseDate() {return releaseDate;}
    public void setReleaseDate(Date releaseDate) {this.releaseDate = releaseDate; }

    public double getLength() {return length;}
    public void setLength(double length) {this.length = length;}

    public int getPopularity() {return popularity;}
    public void setPopularity(int popularity) {
        this.popularity = popularity;
    }

    public double getDanceability() {return danceability;}
    public void setDanceability(double danceability) {
        this.danceability = danceability;
    }

    public double getAcousticness() {return acousticness;}
    public void setAcousticness(double acousticness) {
        this.acousticness = acousticness;
    }

    public double getEnergy() {return energy;}
    public void setEnergy(double energy) {this.energy = energy;}

    public double getInstrumentalness() {return instrumentalness;}
    public void setInstrumentalness(double instrumentalness) {
        this.instrumentalness = instrumentalness;
    }

    public double getLiveness() {return liveness;}
    public void setLiveness(double liveness) {
        this.liveness = liveness;
    }

    public double getLoudness() {return loudness;}
    public void setLoudness(double loudness) {
        this.loudness = loudness;
    }

    public double getSpeechiness() {return speechiness;}
    public void setSpeechiness(double speechiness) {
        this.speechiness = speechiness;
    }

    public double getTempo() {return tempo;}
    public void setTempo(double tempo) {this.tempo = tempo;}

    public int getTimeSignature() {return timeSignature;}
    public void setTimeSignature(int timeSignature) {
        this.timeSignature = timeSignature;
    }

    public boolean isBlacklisted() {return isBlacklisted;}
    public void setBlacklisted(boolean blacklisted) {
        isBlacklisted = blacklisted;
    }

    public String getSpotifyUri() {return spotifyUri;}
    public void setSpotifyUri(String spotifyUri) {
        this.spotifyUri = spotifyUri;
    }

    // Short for testing purposes - add more attributes in the future
    public String toString(){
        return getTrackName();
    }

}
