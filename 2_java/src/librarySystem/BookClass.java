package librarySystem;

import java.util.UUID;

public class BookClass implements Book {

    private String title;
    private Author author;
    private int pages;
    private UUID uid;

    public BookClass(String title, Author author, int pages) {
        this.title = title;
        this.author = author;
        this.pages = pages;
        this.uid = UUID.randomUUID();
    }

    @Override
    public String getTitle() {
        return this.title;
    }

    @Override
    public Author getAuthor() {
        return this.author;
    }

    @Override
    public int getPages() {
        return this.pages;
    }

    @Override
    public UUID getID() {
        return this.uid;
    }

}