# Ingest Failer
> Force a callback timeout for 'stuck' SIPs.

Small GUI utility to force a callback timeout for the British Library's AVSIP Tool ([Audio Visual Submission Information Package](http://armadillosystems.com/index.php/british-library-save-our-sounds/)). 

   ![enter image description here](https://lh3.googleusercontent.com/pw/ACtC-3fa115xjd522lJkEmfIEXACIcxhCWgdRch14C75HxxP6lWkgB9U7qo97sJPwJmVtEqxmnvzBnEw6ACcW3pnYVS9tSEfIJCuUOxYq_W8PX43rti2PyxbZ3qQhlAiTEWr2r2BkbDqpdn9ItqlL34CovnS0A=w357-h256-no)

## Installation

Windows:

```sh
pip install ingest_failer
```
Or use the standalone Windows executables.

## Usage example

Simply enter the SIP ID, press return and the status of the SIP will be shown.

_The SIP has been completed and successfully submitted to the Digital Library System (DLS)_
![Successfully Ingested into the Digital Library System](https://lh3.googleusercontent.com/pw/ACtC-3eM1k4EqLVmow5be4_I0oOXtwdoCxFV8fvyZS9nwBbWShq84AxioeA8_GJn4Jplo0577et4kUVGaG33JHNq2QCSJlHn-Qc2bxuiKe9eMH4Tq1iK5Q9WVzyZW-aLJ8xLB3zJK3f2AOqkYfFX4ivHQ4RCjg=w289-h147-no)


_The SIP has not been completed and is still available to edit in the AVSIP Tool_
![Not yet completed](https://lh3.googleusercontent.com/pw/ACtC-3fNsczBqRFvA0cyog0MdEaLcGwHW0KMUYkLSpVjrrKn4vSTGss7gh4SYSu34ZEr1xQJ2adOskv-IbLIEL9vMNjdqf2H8PUVZapxCs0ldXXsN0nOZU0j6a-xs_pzjo2Xk1MD8uLEuhs9Tgc_rLX3fAh2FA=w289-h147-no)


_The SIP has failed ingest and can be corrected in the AVSIP Tool. The "Details" button gives the last Submission Error Message received._  
![Failed Ingest](https://lh3.googleusercontent.com/pw/ACtC-3fOQH8IVKQWPUzj6KmwKPCJFcwlRHXOhUM8mMhGvxJZBGU0YrnbvTRt6oOr7HAhPEAQG7PPVM4Gr5yRfpWgqbMKVqOHWeCfnPmTwHraE2xB1Cik-4MCIPnWrVTdV0oP--klI7qeaopvjReKrX0AGt29fg=w382-h192-no)


_The SIP has been completed but is still 'stuck' in a state of submission_
![The SIP appears stuck ](https://lh3.googleusercontent.com/pw/ACtC-3doThV0bLNRxOl9y0Qaz4C4vtjkhoYYj8rUE0dFhdbZlOeF-O9Si7thpoxrw6ftnXAUzVIwhUwRBBAH8MG942dgk-Sy6c5brr1_EtsMsbqag9RB9yBmAainC9tIa3F_IzolZRALoHT0Loi7KSThxAbYtg=w206-h147-no)
_N.B - Ingest Failer doesn't check how long a SIP has been stuck for, it simply assumes if you're using the tool there is an issue with the SIP_

![enter image description here ](https://lh3.googleusercontent.com/pw/ACtC-3dg3-ESGcxYY56aXhLPEyM5i_kfBZKEF33OBQQfF9AS4Q59psBmQCycD65OUns1HonDoKXbcYmsu3mCMynfeUGMu1ivnRqoxm6H9cSYpmvkh5PqBDZuTTP6zGvyTwkROF0kLb5vBO93i40nbDW7-Mx68w=w270-h117-no)
## Development setup

Describe how to install all development dependencies and how to run an automated test-suite of some kind. Potentially do this for multiple platforms.

```sh
make install
npm test
```

## Release History

* 0.0.1
    * First Release.

## Meta

Chris Weaver – [@cjohnweaver](https://twitter.com/dbader_org) – christoptopher.weaver@bl.uk

Distributed under the GNU General Public License. See ``LICENSE`` for more information.

[https://github.com/cjweaver/IngestFailer](https://github.com/cjweaver/IngestFailer)

## Contributing

1. Fork it [https://github.com/cjweaver/IngestFailer/fork](https://github.com/cjweaver/IngestFailer)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
