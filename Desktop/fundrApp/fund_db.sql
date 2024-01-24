USE sql6679269;

-- Creating the table
CREATE TABLE fundr_alx (
    ID VARCHAR(255),
    Image VARCHAR(255),
    Amount DECIMAL(10, 2),
    Details TEXT
);
-- Inserting data into the table
INSERT INTO fundr_alx (ID, Image, Amount, Details)
VALUES (
        '1',
        '/home/hadeel/shared/pr1.png',
        960.00,
        'The Smith'
    ),
    (
        '2',
        '/home/hadeel/shared/pr2.png',
        650.00,
        'The Sam'
    ),
    (
        '3',
        '/home/hadeel/shared/pr3.png',
        370.00,
        'The Soy'
    ),
    (
        '4',
        '/home/hadeel/shared/pr4.png',
        840.00,
        'The Sina'
    ),
    (
        '5',
        '/home/hadeel/shared/for1.png',
        260.00,
        'The Jack'
    ),
    (
        '6',
        '/home/hadeel/shared/for2.png',
        140.00,
        'The John'
    ),
    (
        '7',
        '/home/hadeel/shared/for3.png',
        750.00,
        'The Jina'
    ),
    (
        '8',
        '/home/hadeel/shared/for4.png',
        840.00,
        'The Jeem'
    );
SELECT *
FROM fundr_alx;