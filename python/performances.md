# No index

| size         | time (in ms) |
|--------------|--------------|
| 0            | 0-1          |
| 1            | 0-1          |
| 10           | 0-1          |
| 100          | 0-1          |
| 1,000        | 0-1          |
| 10,000       | 1-3          |
| 50,000       | 5-10         |
| 100,000      | 8-15         |
| 1,000,000    | 119-165      |
| 10,000,000   | 968          |
| 100,000,000  | CRASH        |

# with indexgr

| size         | time (in ms) |
|--------------|--------------|
| 0            | 0            |
| 1            | 0-1          |
| 10           | 0-1          |
| 100          | 0-1          |
| 1,000        | 0-1          |
| 10,000       | 1-3          |
| 50,000       | 5-9          |
| 100,000      | 10-18        |
| 1,000,000    | 104-156      |
| 10,000,000   | 860          |
| 100,000,000  |              |


# With optimisation

| size         | time (in ms) |
|--------------|--------------|
| 0            | 0-1          |
| 1            | 0-1          |
| 10           | 0-1          |
| 100          | 0-1          |
| 1,000        | 0-1          |
| 10,000       | 1            |
| 50,000       | 1            |
| 100,000      | 1            |
| 1,000,000    | 1            |
| 10,000,000   | 1            |
| 20,000,000   | 4            |
| 100,000,000  | 2            |
