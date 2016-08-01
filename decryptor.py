from pseudo_prime_check import powerMod
from pseudo_prime_check import isPrime
from pseudo_prime_check import isStrongPseudoprime
import random
import fractions
import math


#This is encryptor. This program encrypts and decrypts integer inputs using public and private keys. It is part of the cyptopye project oon github.
    #Copyright (C) 2016  Edward "Teddy" Zamborsky

    #This program is free software: you can redistribute it and/or modify
    #it under the terms of the GNU General Public License as published by
    #the Free Software Foundation, either version 3 of the License, or
    #(at your option) any later version.

    #This program is distributed in the hope that it will be useful,
    #but WITHOUT ANY WARRANTY; without even the implied warranty of
    #MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    #GNU General Public License for more details.

    #You should have received a copy of the GNU General Public License
    #along with this program.  If not, see <http://www.gnu.org/licenses/>.
    #Contact the author by email at tzamboiv@gmail.com (Public key is available online) or on twitter @tzamboiv


w = "THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY APPLICABLE LAW.  EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM 'AS IS' WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.  THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM IS WITH YOU.  SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF ALL NECESSARY SERVICING, REPAIR OR CORRECTION."
c = "4. Conveying Verbatim Copies.You may convey verbatim copies of the Program's source code as youreceive it, in any medium, provided that you conspicuously andappropriately publish on each copy an appropriate copyright notice;keep intact all notices stating that this License and anynon-permissive terms added in accord with section 7 apply to the code;keep intact all notices of the absence of any warranty; and give allrecipients a copy of this License along with the Program.You may charge any price or no price for each copy that you convey,and you may offer support or warranty protection for a fee.5. Conveying Modified Source Versions.You may convey a work based on the Program, or the modifications toproduce it from the Program, in the form of source code under theterms of section 4, provided that you also meet all of these conditions:  a) The work must carry prominent notices stating that you modified  it, and giving a relevant date.  b) The work must carry prominent notices stating that it is  released under this License and any conditions added under section  7.  This requirement modifies the requirement in section 4 to  'keep intact all notices'.  c) You must license the entire work, as a whole, under this  License to anyone who comes into possession of a copy.  This  License will therefore apply, along with any applicable section 7  additional terms, to the whole of the work, and all its parts,  regardless of how they are packaged.  This License gives no  permission to license the work in any other way, but it does not  invalidate such permission if you have separately received it.  d) If the work has interactive user interfaces, each must display  Appropriate Legal Notices; however, if the Program has interactive  interfaces that do not display Appropriate Legal Notices, your  work need not make them do so.A compilation of a covered work with other separate and independentworks, which are not by their nature extensions of the covered work,and which are not combined with it such as to form a larger program,in or on a volume of a storage or distribution medium, is called an 'aggregate' if the compilation and its resulting copyright are notused to limit the access or legal rights of the compilation's usersbeyond what the individual works permit.  Inclusion of a covered workin an aggregate does not cause this License to apply to the otherparts of the aggregate.6. Conveying Non-Source Forms.You may convey a covered work in object code form under the termsof sections 4 and 5, provided that you also convey themachine-readable Corresponding Source under the terms of this License,in one of these ways:  a) Convey the object code in, or embodied in, a physical product  (including a physical distribution medium), accompanied by the  Corresponding Source fixed on a durable physical medium  customarily used for software interchange.  b) Convey the object code in, or embodied in, a physical product  (including a physical distribution medium), accompanied by a  written offer, valid for at least three years and valid for as  long as you offer spare parts or customer support for that product  model, to give anyone who possesses the object code either (1) a  copy of the Corresponding Source for all the software in the  product that is covered by this License, on a durable physical  medium customarily used for software interchange, for a price no  more than your reasonable cost of physically performing this  conveying of source, or (2) access to copy the  Corresponding Source from a network server at no charge.  c) Convey individual copies of the object code with a copy of the  written offer to provide the Corresponding Source.  This  alternative is allowed only occasionally and noncommercially, and  only if you received the object code with such an offer, in accord  with subsection 6b.  d) Convey the object code by offering access from a designated  place (gratis or for a charge), and offer equivalent access to the  Corresponding Source in the same way through the same place at no  further charge.  You need not require recipients to copy the  Corresponding Source along with the object code.  If the place to  copy the object code is a network server, the Corresponding Source  may be on a different server (operated by you or a third party)  that supports equivalent copying facilities, provided you maintain  clear directions next to the object code saying where to find the  Corresponding Source.  Regardless of what server hosts the  Corresponding Source, you remain obligated to ensure that it is  available for as long as needed to satisfy these requirements.  e) Convey the object code using peer-to-peer transmission, provided  you inform other peers where the object code and Corresponding  Source of the work are being offered to the general public at no  charge under subsection 6d.A separable portion of the object code, whose source code is excludedfrom the Corresponding Source as a System Library, need not beincluded in conveying the object code work. A 'User Product' is either (1) a 'consumer product', which means anytangible personal property which is normally used for personal, family,or household purposes, or (2) anything designed or sold for incorporationinto a dwelling.  In determining whether a product is a consumer product,doubtful cases shall be resolved in favor of coverage.  For a particularproduct received by a particular user, 'normally used' refers to atypical or common use of that class of product, regardless of the statusof the particular user or of the way in which the particular useractually uses, or expects or is expected to use, the product.  A productis a consumer product regardless of whether the product has substantialcommercial, industrial or non-consumer uses, unless such uses representthe only significant mode of use of the product.'Installation Information' for a User Product means any methods,procedures, authorization keys, or other information required to installand execute modified versions of a covered work in that User Product froma modified version of its Corresponding Source.  The information mustsuffice to ensure that the continued functioning of the modified objectcode is in no case prevented or interfered with solely becausemodification has been made.If you convey an object code work under this section in, or with, orspecifically for use in, a User Product, and the conveying occurs aspart of a transaction in which the right of possession and use of theUser Product is transferred to the recipient in perpetuity or for afixed term (regardless of how the transaction is characterized), theCorresponding Source conveyed under this section must be accompaniedby the Installation Information.  But this requirement does not applyif neither you nor any third party retains the ability to installmodified object code on the User Product (for example, the work hasbeen installed in ROM).The requirement to provide Installation Information does not include arequirement to continue to provide support service, warranty, or updatesfor a work that has been modified or installed by the recipient, or forthe User Product in which it has been modified or installed.  Access to anetwork may be denied when the modification itself materially andadversely affects the operation of the network or violates the rules andprotocols for communication across the network.Corresponding Source conveyed, and Installation Information provided,in accord with this section must be in a format that is publiclydocumented (and with an implementation available to the public insource code form), and must require no special password or key forunpacking, reading or copying."

def deconverter(input_long):
    in_string = str(input_long)
    if len(in_string) % 3 == 2:
        in_string = "0" + in_string
    elif len(in_string) % 3 == 1:
        in_string = "00" + in_string
    empt = []
    while len(in_string) != 0:
        thing = in_string[0] + in_string[1] + in_string[2]
        empt.append(thing)
        in_string = in_string[3:]
    end = ""
    for i in empt:
        end = end + chr(long(i))
    return end

def decryptor(n, d, ciph_num):
    #decrypts an integer using d, the private key, and n
    plaintext = pow(ciph_num, d, n)
    return plaintext

n_ = int(input("Enter your public n key: "))
d_ = int(input("Enter your private d key: "))
ciph_ = int(input("Enter the ciphertext: "))
print deconverter(decryptor(n_, d_, ciph_))
