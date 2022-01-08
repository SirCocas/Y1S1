NOTA: algumas quotes têm a citação associada, para se poder, quando se for citar, usar a fonte primária

@inproceedings{subedi2018forensic,
  title={Forensic analysis of ransomware families using static and dynamic analysis},
  author={Subedi, Kul Prasad and Budhathoki, Daya Ram and Dasgupta, Dipankar},
  booktitle={2018 IEEE Security and Privacy Workshops (SPW)},
  pages={180--185},
  year={2018},
  organization={IEEE}
}

infos:
Cyber criminals are using ransomware attacks frequently
because it is very easy to make quick money. Moreover,
the monetary transactions performed remained intractable
due to the use of crypto-currencies like bitcoin.

Similar to malware, ransomware utilizes all types of means
(e.g., spam emails, mal-advertisements, social engineering)
to propagate to a victim’s computing system. Then, it will
either lock the victim’s system (i.e., locker ransomware) or
encrypt the data (i.e., crypto-ransomware) in the victim’s
systems. Finally, it will require the victim to pay the ransom
money in order to unlock the system or obtain the key
for decrypting the data.

In comparison, the
crypto-ransomware is much more harmful than the locker
ransomware, since locker ransomware only locks the victim
system, and the victim can still have access to his/her data
by removing the storage from the infected system to an
uninfected machine. Crypto-ransomware uses cryptographic
encryption algorithms to encrypt the victim’s data and the
key may be stored in a remote C&C server, rendering it
difficult to recover the data without paying the ransom money.

Most of the work on ransomware focuses on dynamic
analysis using sandbox, a technique for running an untrusted
program in safe environment without causing real harm to
the system. Dynamic analysis has several drawbacks; for
example, ransomware may detect the sandbox environment
and may not execute in the sandboxing environment.
Additionally, we are unaware of the arguments required
for some command line malware unless we performed a
thorough analysis. We claim that static analysis and reverse
engineering is required to have through understanding of
ransomware functionalities.

FAMILIES        Propagation Strategy                                Date Appeared   Cryptographic Techniques                C and C Server
REVETON         Accused of illegal activities                       2012            RSA and DES                             Using MoneyPak
GPCODE          Email Attachments                                   2013            660-bit RSA and AES                     Tor Network
CRYPTOLOCKER    compromised websites and email attachments          2013            2048-bit RSA                            Tor Network
CRYPTOWALL      compromised websites and email attachments          2013            2048-bit RSA                            Tor Network
FILECRYPTO      compromised websites and email attachments          2013            2048-bit RSA                            Tor Network
TELSACRYPT      compromised websites and email attachments          2013            2048-bit RSA                            Tor Network
CTB-LOCKER      Email Attachments                                   2014            Elliptic Curve Cryptography             Onion Network
CRYPTOMIX       Spear-phishing Email                                2014            2048-RSA and AES-256 and ROT-13         P-2-P Network
CERBER          compromised websites and email attachments          2013            2048-bit RSA and RC4                    Hardcoded IP range
PETYA           Link in an Email purporting to be a job application 2016            Elliptic Curve Cryptography and Salsa   Tor Network
SATANA          Email Attachments                                   2016            256-bit AES in ECB                      Hardcoded IP Address
JIGSAW          Word Document with Javascript                       2016            RSA and AES                             Onion Network
SHADE           Spam Email                                          2015            RSA-3072 and AES-256                    Fixed Server as C and C server
WANNACRY        Samba Vulnerability                                 2017            RSA and AES combination                 Onion Network

Propagation strategies
provide what types of measures should be implemented to
reduce the risk of the ransomware attacks which includes
security awareness training, secure coding practice, secure
software development life cycle, penetration testing etc. In
addition, incident response team must be vigilant for further
analysis of suspicious email attachments, compromised web
site visits, emails, unpatched applications etc. 

The traditional method of generating signatures based on
the hash function of a malware is not effective for ransomware
since it can be easily bypassed.

...

Indicators associated with wannacry ransomware. https://www.us-cert.
gov/ncas/alerts/TA17-132A. (2021)

Ransomware not only targets home users; businesses can also become infected with ransomware, leading to negative consequences, including
-temporary or permanent loss of sensitive or proprietary information,
-disruption to regular operations,
-financial losses incurred to restore systems and files, and
-potential harm to an organization’s reputation.
-Paying the ransom does not guarantee the encrypted files will be released; it only guarantees that the malicious actors receive the victim’s money, and in some cases, their banking information. In addition, decrypting files does not mean the malware infection itself has been removed.

...

@inproceedings{allix2014forensic,
  title={A Forensic Analysis of Android Malware--How is Malware Written and How it Could Be Detected?},
  author={Allix, Kevin and J{\'e}rome, Quentin and Bissyand{\'e}, Tegawende F and Klein, Jacques and State, Radu and Le Traon, Yves},
  booktitle={2014 IEEE 38th Annual Computer Software and Applications Conference},
  pages={384--393},
  year={2014},
  organization={IEEE}
}

In
recent years, practitioners and researchers have witnessed the
emergence of a variety of Android malware. The associated
threats range from simple user tracking and disclosure of
personal information to advanced fraud and premium-rate
SMS services subscription, or even unwarranted involvement
in botnets. Although most users are nowadays aware that
personal computers can and will be attacked by malware,
very few realize that their smartphone is prone to an equally
dangerous threat.

• We extensively provide evidence that malware labelling
is not a precise science. Applications are flagged or not
depending on the antivirus product;
• We show that most malware writers basically
copy/paste code from fellow developer code and from
public tutorials/samples from the Web;
• We find that malware writing is almost a regular
business, with work cycles following a similar 5
working days per week;
• We also highlight that almost all malware writers are
incapable to properly use digital certificates;

An investigation into the business of malware requires
a significant dataset representing real-world applications.

Malware identification by anti virus products is critical
to practitioners and researchers alike. Indeed, anti virus
products remain the most trusted means to flag an
application as malware. Traditionally, the common detection
scheme of anti virus is signature-based. Thus, to identify
malware statically, antivirus software compares the contents
of application files to their secret dictionary of virus
signatures. This approach can be very effective, but can only
help identify malware for which samples have already been
obtained and associated signatures created. Some antivirus
products add heuristics to their process in order to identify
new malware or variants of known malware

Anti virus software cannot each identify all existing
malware. Only a small subset of widely known
malware are recognized by a large number of anti
virus software.

Despite the potential noise due to the
threshold set by each anti virus to tag malware, we note a
pattern in the compilation dates: it stands out that there are
many more peaks of malware packaging. This suggests that
malware often are compiled in batches, while compilation
of benign applications are more spread over time

Malware development is often a standardized process
that aims at producing a large number of malware
at once. Aside from rare cases of target-specialized
malware, malware are built in bulk in the like of
slightly different applications.

On average, 19% of benign applications are packaged
during weekends, while this is the case for only 13% of
malware. We further use the MWW test to confirm that
the difference between weekdays and week-end days is
statistically more significant for malware than for benign.
There is thus a clear pattern of five-day work per week.

There appear to be evidence that the business of
malware writing, or at least their proliferation, is at
an industrial scale.

Android applications rely on digital certificates to build a
trust model between developers and end users. Applications
signed using the same certificate can share information
and data at runtime (if allowed by explicit permissions).
Certificates also allow to link a set of applications with
their developer, although this linking does not ensure that
the identity of a developer is certified. Indeed, certificates
can be self-signed, rather than signed by a competent
trustworthy authority, and therefore do not necessary lead
to the real developer. However, finding the same certificate
(serial number, fingerprint , issuer and owner) in several
applications is a strong indicator of either a unique origin,
or of advanced certificate stealing and reuse.

Of the 165 542 certificates in our dataset, only 51 are
not self-signed. Self-signed certificates were used to sign
99.88% of the apps in our dataset. Consequently, most
certificates carry no information that could be trusted about
the identity of the application developer.

We further consider the overlap between benign and
malicious applications that share the same certificate. In
Table IV, we indicate the top certificates that are used by
both malware and goodware. We note that there is a clear
overlap showing the usage of certificates for both malicious
and benign applications. A number of explanations can be
provided for this phenomenon:
• Dr Jekyll and Mr Hyde syndrome. Developers use
the same development tools and environment for both
legitimate and malicious applications. This observation
supports the 5 working day behavior shown in table II.
This means that developers write malware during their
regular working hours.
• Reputation biasing. In this hypothesis, a developer
might increase her/his reputation by developing benign
applications. As soon as enough positive reviews
have been obtained, successive malware might be
more easily downloaded and installed. For instance,
the certificate with the serial 4DFF5300, has been
observed signing both a malicious and a non malicious
application on 2011-08-30, in the very same time:
21:52:38. On the overall 1 benign application and 176
malware are associated with this certificate. The most
recent application in our dataset using this certificate
was packaged on 2012-03-11 17:19:54, while its first
usage can be traced back to 2011-07-14 21:45:12.
• Anti virus false negatives. Probably, some of the
applications tagged as benign are in fact malicious. It is
possible that existing tools have not detected them yet
as malicious, due to a better obfuscation and stealthier
behavior.
• Anti virus false positives. Anti virus can also
wrongly flag a benign application as malware.
For instance the digital certificate whose md5
is 75BDB3531C04EB8246846532A7AE2050 has been
observed to sign 2 844 total applications, only one (1)
of which being tagged as malicious. In this case, we
suspect that either the certificate was stolen, but using
it for only one single malicious application does not
really make sense. More probable is the hypothesis that
the single malicious application is a false positive. We
have correlated this information also with the time-line
of the packaging dates for this certificate. The single
malicious application was packaged on 2013-11-15
19:16:04; On this very same day, this certificate signed
55 other apps that are all undetected by anti virus
products. The usage pattern for this certificate shows
very frequent application signing, often with just a
few minutes between two apps, and the application
detected as a malware exhibits no deviation from this
pattern. Furthermore, it would make sense for the
developer to create a new certificate if he once wrote a
malware, in order to avoid having his/her future benign
applications signed with a certificate that is associated
with a malware.

Malware writers do not use digital certificates
properly, and often reuse compromised keys that were
used to build certificates of benign applications.

On Anti virus software: Our large-scale analysis of
hundreds of thousands of Android applications with over
40 anti virus products have revealed that most malware are
not simultaneously identified by several anti virus. Only a
small subset of common malware is detected by most anti
virus software. This finding actually supports the idea that
there is a need to invest in alternative tools for malware
detection such as machine-learning based approaches which
are promising to flag more malware variants.
On malware business: We have presented empirical
evidence that malware were mass produced. This raises
a number of questions leading to hypothesis on how
malware developers manage to remain productive. The first
hypothesis would be that, malware is not written from
scratch, thus providing an opportunity to detect malware by
discovering the piece of code that was grafted to existing,
potentially popular, apps

...

@inproceedings{scaife2016cryptolock,
  title={Cryptolock (and drop it): stopping ransomware attacks on user data},
  author={Scaife, Nolen and Carter, Henry and Traynor, Patrick and Butler, Kevin RB},
  booktitle={2016 IEEE 36th International Conference on Distributed Computing Systems (ICDCS)},
  pages={303--312},
  year={2016},
  organization={IEEE}
}

Solutions to these (malware) attacks require OS modification and are not widely
deployed. A more robust solution would be based on the
detection of the bulk transformation of a user’s data before it
completes, allowing the user to stop such transformation and
denying ransomware access to the totality of the user data.
This “data-centric” approach minimizes the pressure to pay an
adversary as the data loss can be minimized.

The signature behavior of ransomware is its encryption of
the victim’s data. Ransomware must read the original data,
write encrypted data, and remove the original data to complete
this transformation. Note that detecting calls to encryption
libraries alone is not sufficient as many variants implement
their own versions of these algorithms. The specific activities
that ransomware performs can be refined into three classes:

Class A ransomware overwrites the contents of the original
file by opening the file, reading its contents, writing the
encrypted contents in-place, then closing the file. It may optionally rename the file. 
Class B ransomware extends Class A,
with the addition that the malware moves the file out of the
user’s documents directory (e.g., into a temporary directory).
It then reads the contents, writes the encrypted contents, then
moves the file back to the user’s directory. The file name
when moving back to the documents directory may be different
than the original file name. Since the destination file name
may not match the original during any move, the state of
the file must be carefully tracked each time a file is moved.
Class C ransomware reads the original file, then creates a new,
independent file containing the encrypted contents and deletes
or overwrites (via a move) the original file. This class uses
two independent access streams to read and write the data.

...

@inproceedings{roundy2010hybrid,
  title={Hybrid analysis and control of malware},
  author={Roundy, Kevin A and Miller, Barton P},
  booktitle={International Workshop on Recent Advances in Intrusion Detection},
  pages={317--338},
  year={2010},
  organization={Springer}
}

A combination of static
and dynamic analysis allows us to provide analysis-guided instrumentation on
obfuscated, packed, and self-modifying program binaries for the first time. We
implemented these ideas in SD-Dyninst, and demonstrated that they can be
applied to most of the packing tools that are popular with current malware.
We demonstrated the usefulness of our techniques by applying SD-Dyninst to
produce analysis artifacts for the Conficker A binary that would have required
substantial manual effort to produce through alternative methods.

...

@article{oz2021survey,
  title={A Survey on Ransomware: Evolution, Taxonomy, and Defense Solutions},
  author={Oz, Harun and Aris, Ahmet and Levi, Albert and Uluagac, A Selcuk},
  journal={arXiv preprint arXiv:2102.06249},
  year={2021}
}
overall has a lot of info

In recent years, ransomware has been one of the most notorious malware targeting end users, governments,
and business organizations. It has become a very profitable business for cybercriminals with revenues of millions of dollars, and a very serious threat to organizations with financial loss of billions of dollars.

Recent years have witnessed a dramatic growth in the number of incidents a unique malware strain
involved in, namely ransomware. This notorious malware strain has been targeting not only ordinary end users, but also governments and business organizations in almost any sector.

the first ransomware emerged in 1989

First of all,
ransomware typically relies on strong encryption that is very easy to accommodate thanks to several open source implementations. Secondly, it makes use of almost all of the infection techniques
that are employed by modern malware families. Moreover, it benefits from the common evasion
techniques utilized by modern malware (i.e., code obfuscation, encrypted communications, domain generation algorithms (DGA) or fast-fluxing to dynamically shift/generate domain names,
etc.). In addition, it frequently uses application programming interfaces (APIs) provided by victim
platforms to perform its malicious actions that makes it difficult to distinguish ransomware from
benign applications. Furthermore, it uses anonymous communication such as TOR (The Onion
Routing networks) and pseudo-anonymous and unregulated payment techniques like cryptocurrencies that serve attackers to get paid without easily disclosing their identities

A generalized overview of ransomware attack phases is shown in Figure 1. Attack phases of
ransomware can be summarized as follows:
• Infection: In this phase, ransomware is delivered to a victim system (e.g., PC/workstation,
mobile device, IoT/CPS device, etc.). Malicious actors employ several infection vectors to
achieve the delivery of ransomware.
• Communication with C&C servers: After the infection, ransomware connects to the Command and Control (C&C) server to exchange crucial information (i.e., encryption keys, target
system information) with the attacker. Although several ransomware strains communicate
with C&C servers, there exist some families that do not perform any communication.
• Destruction: In this phase, ransomware performs the actual malicious actions such as encrypting files or locking systems to prevent the access of the victim to his/her files or system.
• Extortion: Finally, the ransomware informs the victim about the attack by displaying a ransom note. The ransom note discloses the attack details and payment instructions.
We note that some ransomware families display worm-like behavior, in which they try to infect
more victims that reside in the same network.

In 2014, the increasing popularity of mobile devices triggered the appearance of the first mobile
locker ransomware, namely Android Defender. It was trying to trick users by disguising itself as a
legitimate antivirus application [145]
One year later, the first mobile cryptographic ransomware
arrived. Similar to Android Defender, it was disguised as a benign application. After infection, it
was scanning mobile device’s SD card and encrypting files with specific extensions using AES. The
encryption key was hard-coded in the binary in plain text, so it was trivial for security researchers
to find the corresponding key and decrypt the files [167].

As a new business model on cybercrime, threat of ransomware moved to a new dimension by
the emergence of Ransomware-as-a-Service (RaaS) in 2015. RaaS aimed to provide user-friendly,
and easy-to-modify ransomware kits that could be purchased by anyone on underground markets.

Ransomware can target a variety of victim types. Analyzing the victim types of ransomware
can provide valuable information towards designing practical defense mechanisms. Victims of
ransomware can be divided into two groups: End-users and Organizations.
End-Users were the primary targets for the first ransomware families

Even though for PCs/workstations cryptographic ransomware are more
threatening than locker variants, it is the opposite way for mobile ransomware. The underlying
reason is that, the effect of locker ransomware on PCs/workstation can be avoided most of the
time by removing the hard-drive [168] whereas on mobile devices, the same process is not easy.

Ransomware authors employ the infection techniques that are used for traditional malware to infect their targets. Infection methods of ransomware can be categorized into five groups: malicious
e-mails, SMS or instant messages (IMs), malicious applications, drive-by-download, and vulnerabilities.

C&C servers are frequently used by adversaries to communicate and configure the malware. In the context of ransomware, C&C servers are mainly used by cryptographic ransomware families to send
or receive the encryption key that is used to encrypt the files and/or applications of the victim.

Ransomware families can connect to the C&C server either via hard-coded IP addresses or domains, or dynamically
fast-fluxed/generated/shifted domain names using Domain Generation Algorithms (DGA).
Hard-coded IPs/Domains: Ransomware families can embed hard-coded IP addresses or domains
to their binaries to setup a connection to the C&C server. In this approach, IP address or the domain
remains the same for every attack, and provides a reliable communication for attackers. However,
those hard-coded values can be used by defense systems to create signatures for detection.
Dynamic Domains: Domain Generation Algorithms (DGA) are used by ransomware families in
order to contact C&C servers dynamically. Those algorithms provide a unique domain name to the
server for each communication by fast-fluxing/generating/shifting the domain names. This form
of communication serves to communicate more robustly for ransomware, and firewalls cannot
easily detect it [150].

Locker ransomware families lock system components to prevent the access of victims. Based on
the target, locking ransomware can be divided into three categories: screen locking, browser locking,
and Master Boot Record (MBR) locking.

...

@inproceedings{takeuchi2018detecting,
  title={Detecting ransomware using support vector machines},
  author={Takeuchi, Yuki and Sakai, Kazuya and Fukumoto, Satoshi},
  booktitle={Proceedings of the 47th International Conference on Parallel Processing Companion},
  pages={1--6},
  year={2018}
}
(definição de surface, static e dynamic analysis)
Malware analyses are generally categorized into either of three
types, surface analysis, static analysis, or dynamic analysis, as follows.
In surface analysis, quantified indicators are used to detect software as a suspicious program. To be specific, the hash value or
file type of the software programs, which have been recognized
as malware, are stored in the database, called virus definitions or
signatures. Then, should suspicious programs have the same hash
value or file type as the existing malware in the database, these
programs are detected. The disadvantage of this type is that variants and/or subspecies of the existing malware cannot be detected,
since they have a different hash value from their ancestors due to
the modification of the original source codes.
In static analysis (a.k.a. white box analysis), the source codes of
suspicious software is analyzed without execution. The advantage
of this type is that the suspicious programs are not required to be
executed, and thus, the analysis is safe. In addition, all the functions
in the program are inspected without execution. Since the source
code is inspected line by line, the analysis, unfortunately, take a
long time and requires high leveled skills.
In dynamic analysis (a.k.a. black box analysis), suspicious software is executed and its behavior is analyzed. To do this, suspicious
programs must be executed for analysis, which exposes the network
or computer systems to danger. Therefore, the dynamic analysis is
performed under a controlled environment, such as Sandbox [4].
In commercialized antivirus software, malware are detected by
the combination of the above analyses. The ransomware detection
scheme proposed in this paper is categorized into the dynamic
analysis.

