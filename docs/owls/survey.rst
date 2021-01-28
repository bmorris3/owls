Survey
======

The following text is an excerpt from
`Morris et al. (2017) <https://ui.adsabs.harvard.edu/abs/2017ApJ...848...58M/abstract>`_.

The definition of the :math:`S`-index has the unfortunate property that
its value varies from one instrument to the next for the same intrinsic
flux. Therefore :math:`S`-index measurements must be calibrated against
the stars observed in the Mount Wilson Observatory (MWO) sample before
spectra from different observatories can be compared. In


Calibrating the :math:`S`-index for APO
---------------------------------------

We reduce the raw ARCES spectra with ``IRAF`` methods to subtract
biases, remove cosmic rays, normalize by the flat field, and do the
wavelength calibration with exposures of a thorium-argon lamp [1]_. We
fit the spectrum of an early-type star with a high-order polynomial to
measure the blaze function, and we divide the spectra of HAT-P-11 and
the MWO stars by the polynomial fit to normalize each spectral order.

Next the normalized spectra must be shifted in wavelength into the
rest-frame by removing their radial velocities. We remove the radial
velocity by maximizing the cross-correlation of the ARCES spectra with
PHOENIX model atmosphere spectra (Husser 2013).

To calibrate the ARCES spectra, we follow the calibration procedure
developed in Isaacson (2010) for HIRES. We collect 51
spectra of 30 stars in the Duncan (1991) MWO sample
with the ARC 3.5 m Telescope at APO and the ARCES spectrograph,
including 22 K stars, 7 G stars and one M star.

We measure the :math:`S`-index for these stars by taking the sum of the
flux in the cores of the :math:`H` and :math:`K` features at 3968.47
Å and 3933.66 Å, weighted with a triangular weighting function with
FWHM=\ :math:`1.09`\ Å. We normalize the weighted emission by the flux
in pseudocontinuum regions :math:`R` and :math:`V`, which are 20 Å-wide
bands centered on 3900 and 4000 Å, respectively. Then :math:`S` on the
MWO-calibrated scale is

.. math::

   \begin{aligned}
   S_{APO} &=& \frac{a~H + b~K}{c~R + d~V} \\
   S_{MWO} &=& C_1 S_{APO} + C_2, \label{eqn:s_ind}
   \end{aligned}

where :math:`a,~b,~c,~d, ~C_1` and :math:`C_2` are parameters that can
be tuned to make ARCES :math:`S`-indices match the scale of
:math:`S_{MWO}` (Duncan 1991). Following the example
of Isaacson (2010), we chose values of :math:`a,b,c,d`
so that :math:`S` has roughly equal flux contributions from the
:math:`H` and :math:`K` emission lines, and roughly equal flux from the
:math:`R` and :math:`V` psuedocontinuum regions in the APO spectra. Thus
we set :math:`a = c = 1`, and we choose :math:`b=2` and :math:`d=1`, so
that :math:`H \sim b~K` and :math:`K \sim d~V`.

Since :math:`S` varies over time for each star in the sample, the linear
correlation between the :math:`S_{APO}` and :math:`S_{MWO}` will have
some intrinsic spread. To incorporate this into our model, we adopt the
:math:`\left< S \right>` and the standard deviation of :math:`S` from
Duncan (1991) as the measurement and uncertainty of
the MWO values. We solve for the constants :math:`C_1` and :math:`C_2`
and their uncertainties with Markov Chain Monte Carlo (MCMC)
(Goodman 2010, Foreman-Mackey 2013). We find
:math:`C_1 = 21.26_{-0.83}^{+0.99}` and
:math:`C_2 = 0.009_{-0.009}^{+0.011}`. The
software tools used to calculate calibrated :math:`S`-indices with
spectra from ARCES are publicly available [2]_.

.. [1]
   An ARCES data reduction manual by J. Thorburn is available at
   http://astronomy.nmsu.edu:8000/apo-wiki/attachment/wiki/ARCES/Thorburn_ARCES_manual.pdf

.. [2]
   ARCES Calcium II H & K Analysis Toolkit: https://github.com/bmorris3/arces_hk