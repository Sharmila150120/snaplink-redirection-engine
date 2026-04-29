SnapLink: Redirection & Analytics Engine
SnapLink is a high-performance URL shortening service that transforms long, complex URLs into manageable, 6-character unique identifiers. It functions as a "Traffic Controller," mapping short codes to destination URLs in a relational database and handling real-time browser redirections.

🛠️ The System Architecture
This project demonstrates the core principles of System Mapping and Database Management:

Hashing/Encoding: Generates unique alpha-numeric IDs for every link to prevent data overlap.

Persistence: Uses a SQLite database (SQLAlchemy ORM) to store the mapping between short IDs and original URLs.

HTTP Redirection: Implements 302 Redirect logic to forward users instantly to their destination.

✨ Key Features
URL Compression: Turns 200+ character URLs into 6-character "snaps."

Collision Resistance: Logic ensures every link gets a unique identifier.

Relational Mapping: Built with SQLAlchemy for efficient data retrieval and storage.

Industrial UI: A modern, dark-mode dashboard designed with Tailwind CSS for high usability.

🚀 Tech Stack
Backend: Python 3.x, Flask

Database: SQLAlchemy (ORM), SQLite

Frontend: Tailwind CSS, HTML5

📊 Why this is useful
Marketing Tracking: Companies use different short links to measure click-through rates (CTR) across different platforms (Instagram vs. Twitter).

Branding: Masking ugly tracking links with clean, professional-looking URLs.

Data Analytics: Acting as a middle-man to count clicks and analyze traffic before sending the user to the destination.
