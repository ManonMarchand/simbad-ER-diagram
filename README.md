# Simbad Entity Relation Diagram

This repository explores two softwares: 

## Mermaid 

https://github.com/mermaid-js/mermaid

```mermaid
%%{init: {"flowchart": {"defaultRenderer": "elk"}} }%%
erDiagram
    OTYPE }o..o{ BASIC : ""
    IDS }o..o{ BASIC : ""
    OTYPES }o..o{ BASIC : ""
    OTYPEDEF }o..o{ OTYPE : ""
    OTYPEDEF }o..o{ BASIC : ""
    IDENT }o..o{ BASIC : ""
    FLUX }o..o{ BASIC : ""
    FLUX }o..o{ FILTER : ""
    ALLFLUXES }o..o{ BASIC : ""
    HASREF }o..o{ REF : ""
    HASREF }o..o{ BASIC : ""
    AUTHOR }o..o{ REF : ""
    MESDISTANCE }o..o{ BASIC : ""
    MESDIAMETER }o..o{ BASIC : ""
    MESFE_H }o..o{ BASIC : ""
    MESISO }o..o{ BASIC : ""
    MESIUE }o..o{ BASIC : ""
    MK }o..o{ BASIC : ""
    MESPLX }o..o{ BASIC : ""
    MESPM }o..o{ BASIC : ""
    MESROT }o..o{ BASIC : ""
    MESVAR }o..o{ BASIC : ""
    MESVELOCITIES }o..o{ BASIC : ""
    MESXMM }o..o{ BASIC : ""
    MESHERSCHEL }o..o{ BASIC : ""
    BIBLIO }o..o{ BASIC : ""
    KEYWORDS }o..o{ REF : ""
    REF }o..o{ JOURNAL : ""
    ALLFLUXES {
        DOUBLE J  ""
        DOUBLE U  ""
        DOUBLE B  ""
        DOUBLE V  ""
        DOUBLE R  ""
        DOUBLE I  ""
        DOUBLE H  ""
        BIGINT oidref  "Object internal identifier"
        DOUBLE K  ""
        DOUBLE u_  ""
        DOUBLE g_  ""
        DOUBLE r_  ""
        DOUBLE i_  ""
        DOUBLE z_  ""
        DOUBLE G  ""
}
    ALLTYPES {
        CLOB otypes  "List of all object types concatenated with pipe"
        BIGINT oidref  "Object internal identifier"
}
    AUTHOR {
        BIGINT oidbibref  "Bibcode internal identifier"
        VARCHAR name  "Author of a bibliographical reference"
        SMALLINT pos  "Position of the author in the bib ref"
}
    BASIC {
        BIGINT oid  "Object internal identifier"
        INTEGER nbref  "number of references"
        SMALLINT ra_prec  "Right ascension precision"
        SMALLINT dec_prec  "Declination precision"
        REAL coo_err_maj  "Coordinate error major axis"
        SMALLINT coo_err_maj_prec  "Coordinate error major axis precision"
        REAL coo_err_min  "Coordinate error minor axis"
        SMALLINT coo_err_min_prec  "Coordinate error minor axis precision"
        SMALLINT coo_err_angle  "Coordinate error angle"
        CHAR coo_qual  "Coordinate quality"
        CHAR coo_wavelength  "Wavelength class for the origin of the coordinates (R,I,V,U,X,G)"
        CHAR coo_bibcode  "Coordinate reference"
        DOUBLE pmra  "Proper motion in RA"
        SMALLINT pmra_prec  "Proper motion in RA precision"
        DOUBLE pmdec  "Proper motion in DEC"
        SMALLINT pmdec_prec  "Proper motion in DEC precision"
        REAL pm_err_maj  "Proper motion error major axis"
        SMALLINT pm_err_maj_prec  "Proper motion error major axis precision"
        REAL pm_err_min  "Proper motion error minor axis"
        SMALLINT pm_err_min_prec  "Proper motion error minor axis precision"
        SMALLINT pm_err_angle  "Proper motion error angle"
        CHAR pm_qual  "Proper motion quality"
        CHAR pm_bibcode  "Proper motion reference"
        DOUBLE plx_value  "Parallax"
        SMALLINT plx_prec  "Parallax precision"
        REAL plx_err  "Parallax error"
        SMALLINT plx_err_prec  "Parallax error precision"
        CHAR plx_qual  "Parallax quality"
        CHAR plx_bibcode  "Parallax reference"
        CHAR rvz_type  "Radial velocity / redshift type"
        DOUBLE rvz_radvel  "Radial Velocity"
        SMALLINT rvz_radvel_prec  "Radial velocity precision"
        DOUBLE rvz_redshift  "redshift"
        SMALLINT rvz_redshift_prec  "redshift precision"
        SMALLINT rvz_err_prec  "Radial velocity / redshift error precision"
        CHAR rvz_qual  "Radial velocity / redshift quality"
        CHAR rvz_bibcode  "Radial velocity / redshift reference"
        VARCHAR sp_type  "MK spectral type"
        CHAR sp_qual  "Spectral type quality"
        CHAR sp_bibcode  "spectral type reference"
        VARCHAR morph_type  "Morphological type"
        CHAR morph_qual  "Morphological type quality"
        CHAR morph_bibcode  "morphological type reference"
        REAL galdim_majaxis  "Angular size major axis"
        SMALLINT galdim_majaxis_prec  "Angular size major axis precision"
        REAL galdim_minaxis  "Angular size minor axis"
        SMALLINT galdim_minaxis_prec  "Angular size minor axis precision"
        SMALLINT galdim_angle  "Galaxy ellipse angle"
        CHAR galdim_qual  "Galaxy dimension quality"
        CHAR galdim_bibcode  "Galaxy dimension reference"
        BIGINT hpx  "Healpix number at ORDER=10"
        CHAR vlsr_wavelength  "Wavelength class for the origin of the LSR velocity"
        CHAR vlsr_bibcode  "Reference for the origin of the LSR velocity"
        REAL vlsr_min  "Minimum for the mean value of the LSR velocity"
        REAL vlsr_max  "Maximum for the mean value of the LSR velocity"
        date update_date  "Date of last modification"
        DOUBLE vlsr  "velocity in Local Standard of Rest reference frame"
        CHAR rvz_nature  "velocity / redshift nature"
        REAL rvz_err  "Radial velocity / redshift error"
        VARCHAR otype  "Object type"
        VARCHAR main_id PK "Main identifier for an object"
        DOUBLE ra PK "Right ascension"
        DOUBLE dec PK "Declination"
        VARCHAR otype_txt PK "Object type"
}
    BIBLIO {
        BIGINT oidref  "Object internal identifier"
        TEXT biblio  "List of Bibcodes separated with a pipe"
}
    CAT {
        VARCHAR cat_name  "Catalogue name"
        INTEGER size  "Number of objects of the Catalogue in SIMBAD"
}
    FILTER {
        UNICODECHAR description  "flux filter description"
        VARCHAR filtername  "flux filter name"
        VARCHAR unit  "physical unit name"
}
    FLUX {
        BIGINT oidref  "Object internal identifier"
        VARCHAR filter  "flux filter name"
        SMALLINT flux_prec  "flux precision"
        REAL flux_err  "flux error"
        SMALLINT flux_err_prec  "flux error precision"
        CHAR qual  "flux quality flag"
        CHAR bibcode  "flux reference"
        REAL flux  ""
}
    H_LINK {
        CHAR link_bibcode  "link reference"
        BIGINT parent  "parent oid"
        BIGINT child  "child oid"
        SMALLINT membership  "membership probability"
}
    HAS_REF {
        BIGINT oidbibref  "Bibcode internal identifier"
        BIGINT oidref  "Object internal identifier"
        VARCHAR ref_raw_id  "id like it appears in the article"
        SMALLINT ref_flag  "flag"
        SMALLINT obj_freq  "flag"
}
    IDENT {
        BIGINT oidref  "Object internal identifier"
        VARCHAR id  "Identifier"
}
    IDS {
        CLOB ids  "List of all identifiers concatenated with pipe"
        BIGINT oidref  "Object internal identifier"
}
    JOURNALS {
        VARCHAR journal  "Abbreviation for the journal"
        VARCHAR years  "Range of years of this journal in the database"
        VARCHAR name  "Full name of the journal"
}
    KEYWORDS {
        UNICODECHAR keyword  "Keyword text and link"
        BIGINT oidbibref  "Object internal identifier of reference"
        INTEGER position  "Position of the keyword in the publication"
}
    MESDIAMETER {
        BIGINT oidref  "Object internal identifier"
        SMALLINT mespos  "Position of a measurement in a list of measurements"
        DOUBLE diameter  "Diameter value"
        SMALLINT diameter_prec  "Precision (# of decimal positions) associated with the column diameter"
        CHAR qual  "Quality"
        CHAR unit  "Unit (mas/km)"
        DOUBLE error  "Error"
        SMALLINT error_prec  "Precision (# of decimal positions) associated with the column error"
        CHAR filter  "filter or wavelength"
        CHAR method  "calculation method"
        CHAR bibcode  "measurement bibcode"
}
    MESDISTANCE {
        BIGINT oidref  "Object internal identifier"
        SMALLINT mespos  "Position of a measurement in a list of measurements"
        DOUBLE dist  "Distance value"
        SMALLINT dist_prec  "Precision (# of decimal positions) associated with the column dist"
        CHAR qual  "Quality"
        CHAR unit  "Unit (pc,kpc or Mpc)"
        DOUBLE minus_err  "minus error"
        SMALLINT minus_err_prec  "Precision (# of decimal positions) associated with the column minus_err"
        DOUBLE plus_err  "plus error"
        SMALLINT plus_err_prec  "Precision (# of decimal positions) associated with the column plus_err"
        CHAR method  "distance calculation method"
        CHAR bibcode  "measurement bibcode"
}
    MESFE_H {
        BIGINT oidref  "Object internal identifier"
        SMALLINT mespos  "Position of a measurement in a list of measurements"
        INTEGER teff  "Effective Temperature"
        REAL log_g  "Decimal logarithm of the surface gravity"
        SMALLINT log_g_prec  "Precision (# of decimal positions) associated with the column log_g"
        REAL fe_h  "Metallicity index relative to the Sun"
        SMALLINT fe_h_prec  "Precision (# of decimal positions) associated with the column fe_h"
        CHAR flag  "Flag on the [Fe/H] value"
        CHAR compstar  "Designates the comparison star from which the [Fe/H] value was obtained"
        CHAR catno  "Star in the Cayrel et al. (1997A&AS..124..299C) compilation"
        CHAR bibcode  "measurement bibcode"
}
    MESHERSCHEL {
        CHAR alpha  "Right Ascension J2000"
        CHAR delta  "Declination J2000"
        SMALLINT mespos  "Position of a measurement in a list of measurements"
        CHAR obsid  "Observation identifier"
        BIGINT oidref  "Object internal identifier"
}
    MESISO {
        BIGINT oidref  "Object internal identifier"
        SMALLINT mespos  "Position of a measurement in a list of measurements"
        CHAR obsid  "Observation identifier"
        DOUBLE ra  "Right ascension"
        SMALLINT ra_prec  "Precision (# of decimal positions) associated with the column ra"
        DOUBLE dec  "Declination"
        SMALLINT dec_prec  "Precision (# of decimal positions) associated with the column dec"
}
    MESIUE {
        BIGINT oidref  "Object internal identifier"
        SMALLINT mespos  "Position of a measurement in a list of measurements"
        CHAR name  "Homogenized Name"
        CHAR complid  "Complementary Identifier"
        CHAR progid  "Observing Program Identification"
        SMALLINT classcode  "IUE class code"
        CHAR dispcode  "Dispersion code"
        CHAR camid  "Camera id"
        INTEGER image  "Image number"
        CHAR aperture  "Aperture designation code"
        INTEGER fescount  "FES count"
        CHAR fesmode  "FES mode"
        CHAR obsdate  "Observation date"
        CHAR obstime  "Observation time"
        INTEGER exptime  "Effective exposure time"
        CHAR abnormcode  "Abnormality code"
        CHAR expqualcode  "Exposure quality code"
        CHAR station  "Station (V=Vilspa/G=Goddard)"
        CHAR comments  "Comments"
        CHAR flag  "Flag"
        CHAR bibcode  "measurement bibcode"
}
    MESPLX {
        BIGINT oidref  "Object internal identifier"
        SMALLINT mespos  "Position of a measurement in a list of measurements"
        REAL plx  "Parallaxe"
        SMALLINT plx_prec  "Precision (# of decimal positions) associated with the column plx"
        SMALLINT plx_err  "sigma{plx}"
        CHAR obscode  "Observatory code"
        CHAR bibcode  "measurement bibcode"
}
    MESPM {
        BIGINT oidref  "Object internal identifier"
        SMALLINT mespos  "Position of a measurement in a list of measurements"
        REAL pmra  "Proper motion R.A."
        SMALLINT pmra_prec  "Precision (# of decimal positions) associated with the column pmra"
        REAL pmra_err  "sigma{pm-ra}"
        SMALLINT pmra_err_prec  "Precision (# of decimal positions) associated with the column pmra_err"
        REAL pmde  "Proper motion DEC."
        SMALLINT pmde_prec  "Precision (# of decimal positions) associated with the column pmde"
        REAL pmde_err  "sigma{pm-de}"
        SMALLINT pmde_err_prec  "Precision (# of decimal positions) associated with the column pmde_err"
        CHAR coosystem  "coordinates system designation"
        CHAR bibcode  "measurement bibcode"
}
    MESROT {
        BIGINT oidref  "Object internal identifier"
        SMALLINT mespos  "Position of a measurement in a list of measurements"
        CHAR upvsini  "Upper value of Vsini"
        REAL vsini  "V sini"
        SMALLINT vsini_prec  "Precision (# of decimal positions) associated with the column vsini"
        REAL vsini_err  "error"
        SMALLINT vsini_err_prec  "Precision (# of decimal positions) associated with the column vsini_err"
        SMALLINT nbmes  "Number of measurements"
        CHAR qual  "Quality"
        CHAR bibcode  "measurement bibcode"
}
    MESSPT {
        BIGINT oidref  "Object internal identifier"
        SMALLINT mespos  "Position of a measurement in a list of measurements"
        CHAR dispsystem  "dispersive system"
        CHAR mssnote  "mss notes"
        CHAR sptype  "MK/MSS spectral type"
        CHAR bibcode  "measurement bibcode"
}
    MESVAR {
        DOUBLE period  "Period"
        BIGINT oidref  "Object internal identifier"
        SMALLINT mespos  "Position of a measurement in a list of measurements"
        CHAR vartyp  "Type of variability"
        CHAR lowVmax  "Upper limit flag for Vmax"
        REAL vmax  "Maximum of brightness"
        SMALLINT vmax_prec  "Precision (# of decimal positions) associated with the column vmax"
        CHAR r_vmax  "Uncertainty flag"
        CHAR magtyp  "Magnitude type"
        CHAR uppVmin  "Lower limit flag for Vmin"
        REAL vmin  "Minimum of brightness"
        SMALLINT vmin_prec  "Precision (# of decimal positions) associated with the column vmin"
        CHAR r_vmin  "Uncertainty flag for Vmin"
        CHAR upperiod  "Lower limit flag for the period"
        SMALLINT period_prec  "Precision (# of decimal positions) associated with the column period"
        CHAR r_period  "Uncertainty flag on period (:)"
        DOUBLE epoch  "Epoch of maximum or minimum"
        SMALLINT epoch_prec  "Precision (# of decimal positions) associated with the column epoch"
        CHAR r_epoch  "Uncertainty on epoch (:)"
        REAL raisingTime  "Raising time for all other variable types"
        SMALLINT raisingTime_prec  "Precision (# of decimal positions) associated with the column raisingTime"
        CHAR r_raisingTime  "Uncertainty flag on raising time"
        CHAR bibcode  "measurement bibcode"
}
    MESVELOCITIES {
        BIGINT oidref  "Object internal identifier"
        SMALLINT mespos  "Position of a measurement in a list of measurements"
        CHAR velType  "velocity type (v, z or cz)"
        DOUBLE velValue  "Velocity"
        SMALLINT velValue_prec  "Precision (# of decimal positions) associated with the column velValue"
        CHAR remark  "colon is uncertain question mark is questionable"
        REAL meanError  "sigma(Value)"
        SMALLINT meanError_prec  "Precision (# of decimal positions) associated with the column meanError"
        CHAR quality  "Quality"
        SMALLINT nbmes  "Number of measurements"
        CHAR nature  "nature of the measurement"
        CHAR qual  "Quality"
        CHAR wdomain  "Wavelength domain (Rad,mm,IR,Opt,UV,XRay,Gam)"
        INTEGER resolution  "Resolution"
        CHAR d  "'D' if the resolution is a conversion from the dispersion"
        DOUBLE obsdate  "Observation date"
        SMALLINT obsdate_prec  "Precision (# of decimal positions) associated with the column obsdate"
        CHAR remarks  "Remarks"
        CHAR origin  "Origin of the radial velocity"
        CHAR bibcode  "measurement bibcode"
}
    MESXMM {
        BIGINT oidref  "Object internal identifier"
        SMALLINT mespos  "Position of a measurement in a list of measurements"
        CHAR obsid  "Observation identifier"
}
    OTYPEDEF {
        VARCHAR path  "Otype path in the hierarchical classification"
        VARCHAR otype PK "Object type"
        VARCHAR label  "Object type, compact label string"
        SMALLINT is_candidate  "True if the object type is a candidate (non-confirmed)"
        VARCHAR otype_shortname  "(DEPRECATED) Object type, short name"
        UNICODECHAR description  "Object type, full description string"
        UNICODECHAR comment  "Additional comment"
        UNICODECHAR otype_longname  "(DEPRECATED) Object type, full description string"
}
    OTYPES {
        BIGINT oidref  "Object internal identifier"
        VARCHAR(30) origin  "explanation of origin of this type"
        VARCHAR otype  "Object type"
        VARCHAR(10) otype_txt  "Object type"
}
    REF {
        BIGINT oidbib  "Bibcode internal identifier"
        CHAR bibcode  "Bibcode"
        SMALLINT year  "Publication year"
        VARCHAR journal  "Abbreviation for the journal"
        INTEGER page  "page number"
        INTEGER last_page  "Last page number"
        INTEGER volume  "volume number"
        CLOB title  "Title"
        VARCHAR doi  "DOI designation"
        INTEGER nbobject  "Number of objects studied in"
        UNICODECHAR abstract  "(revisited) Abstract of published paper"
}

```

## And graphviz

https://gitlab.com/graphviz/graphviz

![simbad-er](simbad-er.svg)
