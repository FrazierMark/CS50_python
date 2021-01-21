-- Keep a log of any SQL queries you execute as you solve the mystery.
--Starting my invistigation with the police report from the location of the theft.

SELECT description
FROM crime_scene_reports
WHERE street = 'Chamberlin Street'
AND month = 7
AND day = 28
AND year = 2020
--RESULTS
--"Theft of the CS50 duck took place at 10:15am at the Chamberlin Street courthouse.
--Interviews were conducted today with three witnesses who were present at the time
--— each of their interview transcripts mentions the courthouse."

--NOTES-- 3 Witness, all mention courthouse.
-- Need to get their transcripts from the interviews to get more information
--about what they witnessed.

SELECT name, transcript
FROM INTERVIEWS
WHERE transcript LIKE '%courthouse%'
AND month = 7
AND day = 28
AND year = 2020

--RESULTS
--Ruth | Sometime within ten minutes of the theft, I saw the thief get into a car
--in the courthouse parking lot and drive away. If you have security footage from
--the courthouse parking lot, you might want to look for cars that left the parking
--lot in that time frame.

--Eugene | I don't know the thief's name, but it was someone I recognized. Earlier
--this morning, before I arrived at the courthouse, I was walking by the ATM on
--Fifer Street and saw the thief there withdrawing some money.

--Raymond | As the thief was leaving the courthouse, they called someone who
--talked to them for less than a minute. In the call, I heard the thief say that
-- were planning to take the earliest flight out of Fiftyville tomorrow. The
--thief then asked the person on the other end of the phone to purchase the flight
--ticket.

--NOTES
--Persuing Ruth's lead. Querying the security logs for license_plate info.

SELECT license_plate
FROM courthouse_security_logs
WHERE minute BETWEEN 15 AND 25
AND day = 28
AND year = 2020
AND hour = 10
AND month = 7
AND activity = 'exit'

--RESULTS
--License plate numbers
--5P2BI95, 94KL13X, 6P58WS2, 4328GD8, G412CB7, L93JTIZ, 322W7JE, 0NTHK55

--NOTES
--I have a list of license plates I can use to narrow down my suspects if I
--query the people table. Name, phone number, and passport seem to be useful info.

SELECT name, phone_number, passport_number
FROM people
WHERE license_plate IN (SELECT license_plate
                       FROM courthouse_security_logs
                        WHERE minute BETWEEN 5 AND 25
                        AND day = 28
                        AND year = 2020
                        AND hour = 10
                        AND month = 7
                        AND activity = 'exit')

--^ Same as below

SELECT DISTINCT(people.name)
FROM people
JOIN courthouse_security_logs
    ON courthouse_security_logs.license_plate = people.license_plate
WHERE courthouse_security_logs.license_plate IN ('5P2BI95', '94KL13X', '6P58WS2', '4328GD8', 'G412CB7', 'L93JTIZ', '322W7JE', '0NTHK55')

--RESULTS
--name | phone_number | passport_number
--Patrick | (725) 555-4692 | 2963008352
--Amber | (301) 555-4174 | 7526138472
--Elizabeth | (829) 555-5269 | 7049073643
--Roger | (130) 555-0289 | 1695452385
--Danielle | (389) 555-5198 | 8496433585
--Russell | (770) 555-1861 | 3592750733
--Evelyn | (499) 555-9472 | 8294398571
--Ernest | (367) 555-5533 | 5773159633

--Here is a list of suspects that all left the court house within 10mins of the
--crime.

--Going to get more information following Eugene's tip. Things to consider,
--Theif WITHDREW money BEFORE the theft at ATM on FIFER Street. Going to
-- query the atm_transactions on FIFER street

SELECT account_number
FROM atm_transactions
WHERE atm_location = "Fifer Street"
AND transaction_type = "withdraw"
AND day = 28
AND year = 2020
AND month = 7

--RESULTS
--Account_numbers
--28500762, 28296815, 76054385, 49610011, 16153065, 25506511, 81061156, 26013199
SELECT *
FROM bank_accounts
WHERE account_number IN (28500762, 28296815, 76054385, 49610011, 16153065, 25506511, 81061156, 26013199)

--Results - 686048
49610011 | 686048 | 2010
26013199 | 514354 | 2012
16153065 | 458378 | 2012
28296815 | 395717 | 2014
25506511 | 396669 | 2014
28500762 | 467400 | 2014
76054385 | 449774 | 2015
81061156 | 438727 | 2018


SELECT name
FROM people
WHERE id IN (686048, 514354, 458378, 395717, 396669, 467400, 449774, 438727)
--RESULTS --- license plate logs

SHORT list after subtracting license plates from atm people
Elizabeth
Danielle
Russell
Ernest

--NOTES
--List of possible suspect's account numbers that were at the atm. Going to query
--the back_accounts to find account_numbers and person_id

SELECT *
FROM people
WHERE name IN ("Elizabeth", "Danielle", "Russell", "Ernest")
Getting full info on suspects
id | name | phone_number | passport_number | license_plate
396669 | Elizabeth | (829) 555-5269 | 7049073643 | L93JTIZ
467400 | Danielle | (389) 555-5198 | 8496433585 | 4328GD8
514354 | Russell | (770) 555-1861 | 3592750733 | 322W7JE
686048 | Ernest | (367) 555-5533 | 5773159633 | 94KL13X


--NOTES
--Going to see who placed a call for less than 1 min on day of crime
SELECT *
FROM phone_calls
WHERE duration <= 60
AND caller IN ("(829) 555-5269", "(389) 555-5198", "(770) 555-1861", "(367) 555-5533")
AND day = 28

--UPdated short list of suspects
514354 | Russell | (770) 555-1861 | 3592750733 | 322W7JE-- 255 | (770) 555-1861 | (725) 555-3243 | 2020 | 7 | 28 | 49
686048 | Ernest | (367) 555-5533 | 5773159633 | 94KL13X -- 233 | (367) 555-5533 | (375) 555-8161 | 2020 | 7 | 28 | 45

--NOTES
--Need to get flight-ID and check destination airport in flights to narrow down.

SELECT *
FROM passengers
WHERE passport_number IN (3592750733, 5773159633)
--Notes, 4 seperate flights, but I know they are leaving the following day on the earliest flight
18 | 3592750733 | 4C
24 | 3592750733 | 2C
36 | 5773159633 | 4A
54 | 3592750733 | 6C

SELECT *
FROM flights
WHERE month = 7
AND day = 29
AND id IN (18, 24, 36, 54)

18 | 8 | 6 | 2020 | 7 | 29 | 16 | 0
36 | 8 | 4 | 2020 | 7 | 29 | 8 | 20
Earlier flight is to >>>>>>> London <<<<<

--Going to backtrack to narrow suspect to 1.
FLIGHT >> 36 | 5773159633 | 4A
Ernest is our suspect with Passport 5773159633.

--Need to find out who he called earlier in the day.

SELECT receiver
FROM phone_calls
Where caller = "(367) 555-5533"
AND duration <= 60

--Results
(375) 555-8161
(455) 555-5315

SELECT *
FROM people
WHERE phone_number IN ("(375) 555-8161", "(455) 555-5315")

--Notes
more info on accomplice suspects
id | name | phone_number | passport_number | license_plate
639344 | Charlotte | (455) 555-5315 | 7226911797 | Z5FH038
864400 | Berthold | (375) 555-8161 |  | 4V16VO0

--GOing to search to see which of these people are on that same flight. 
--Berthold has no passport_number, going to see if Charlotte is traveling.

SELECT *
FROM passengers
Where passport_number = 7226911797

--Results
5 | 7226911797 | 8D
26 | 7226911797 | 9A
42 | 7226911797 | 2B

--Notes
--Non of the above flights leave on the 29th. Our accomplice is BERTHOLD!!