package librarySystem;

import java.util.UUID;

public interface Book {

    /**
     * Retrieve the book title.
     * 
     * @return book title
     */
    String getTitle();

    /**
     * Retrieve the book author.
     * 
     * @return book author
     */
    Author getAuthor();

    /**
     * Retrieve the book page count.
     * 
     * @return book page count
     */
    int getPages();

    /**
     * Retrieve the book unique identifier
     * 
     * @return book identifier
     */
    UUID getID();

}