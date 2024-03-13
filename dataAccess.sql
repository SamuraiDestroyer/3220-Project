-- Canadian Citizen
CREATE TABLE CanadianCitizen (
    citizenID INT AUTO_INCREMENT PRIMARY KEY,
    firstName VARCHAR(255),
    lastName VARCHAR(255),
    email VARCHAR(255) UNIQUE,
    passwordHash VARCHAR(255)
);

CREATE TABLE OpenData (
    dataID INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    description TEXT,
    url VARCHAR(255) -- URL to access the data
);

CREATE TABLE APIStore (
    apiID INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    description TEXT,
    accessURL VARCHAR(255) -- URL to access the API
);
-- developer table
CREATE TABLE Developer (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE Skill (
    id INT AUTO_INCREMENT PRIMARY KEY,
    skill_name VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE DeveloperSkill (
    developer_id INT,
    skill_id INT,
    PRIMARY KEY (developer_id, skill_id),
    FOREIGN KEY (developer_id) REFERENCES Developer(id) ON DELETE CASCADE,
    FOREIGN KEY (skill_id) REFERENCES Skill(id) ON DELETE CASCADE
);

CREATE TABLE DeveloperOpenData (
    developerID INT,
    dataID INT,
    PRIMARY KEY (developerID, dataID),
    FOREIGN KEY (developerID) REFERENCES Developer(id) ON DELETE CASCADE,
    FOREIGN KEY (dataID) REFERENCES OpenData(dataID) ON DELETE CASCADE
);

-- Government Administrator
CREATE TABLE GovernmentAdministrator (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    department VARCHAR(255)
);